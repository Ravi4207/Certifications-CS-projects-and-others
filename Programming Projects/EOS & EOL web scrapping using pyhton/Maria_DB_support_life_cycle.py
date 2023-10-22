import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import urllib3
# to ignore the SSL verification warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_MariaDB_data():

    try:
        url = "https://mariadb.org/about/#maintenance-policy"
        # get the HTML 
        resp = requests.get(url , verify=False)
        htmlContent = resp.content

        soup = BeautifulSoup(htmlContent , 'html.parser')
        tables = soup.find_all('table')

        # Extract the table headers

        # headers = ["Vendor","Product" ,"Release series","Stable (GA) Date" , "End of life"]
        rows = []

        # get the table data
        for i in tables:

            # try:
            #     # get the table header
            #     # for th in i.find_all("th"):
            #     #     headers.append(th.text.strip())
            # except Exception as e:
            #     print("Could not retrive table header")
            #     print("Error occured ",e)
            
            try:
                # get the table row data
                for tr in i.find_all("tr")[1:]:
                    row = []
                    row.append("MariaDB")
                    row.append("MariaDB")
                    for td in tr.find_all("td"):
                        row.append(td.text.strip())

                    rows.append(row)
            except Exception as e:
                print("Could not retrive table row")
                print("Error occured ",e)

        # change the Stable and end of life date format from "11 Apr 2012" format to "11/04/2012"
        try:
            for data in rows:
                try:
                    Stable_Date = data[3]
                    # change Stable date format 
                    if len(Stable_Date) < 12:
                        # create date object 
                        Stable_obj = datetime.strptime(Stable_Date, '%d %b %Y')
                        # pasrse date object to strftime method to format the date
                        Stable_Date = Stable_obj.strftime('%d/%m/%Y')
                    else:
                        Stable_Date = ''
                    data[3] = Stable_Date
                except Exception as e:
                    print("Could not change the date format for Stable Date")
                    print("Error occured ",e)
                
                try:
                    end_of_life = data[4]
                    # change end of life date format
                    # if string length is greater than 11 that means it is not a date
                    if len(end_of_life) < 12:
                        # create date object 
                        end_of_life_obj = datetime.strptime(end_of_life, '%d %b %Y')
                        # parse date object to strftime method to format the date
                        end_of_life = end_of_life_obj.strftime('%d/%m/%Y')
                    else:
                        end_of_life = ''
                    data[4] = end_of_life
                except Exception as e:
                    print("Could not change the date format for end of life Date")
                    print("Error occured ",e)

        except Exception as e:
            print("Could not change the date format")
            print("Error occured ",e)
            
        # save data to csv file 

        with open("Maria_DB_eol_data.csv" , mode="w", newline='') as f:
            csv_writer = csv.writer(f)
            # csv_writer.writerow(headers[0:5])
            for r in rows:
                csv_writer.writerow(r)
        print("Table data has been saved to Maria_DB_eol_data.csv")

    except Exception as e:
        print("Could not get the data for MariaDB")
        print("Error occured ", e)
        
