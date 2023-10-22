import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import urllib3
# to ignore the SSL verification warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.dell.com/support/kbdoc/en-in/000128563/end-of-life-end-of-support-policy-for-dell-data-security"

def get_dell_data():
    try:
        # get the HTML page content
        resp = requests.get(url , verify=False)
        htmlContent = resp.content
        # create soup object
        soup = BeautifulSoup(htmlContent , 'html.parser')
        # get tables 
        tables = soup.find_all('table')
        num = 0
        # headers = ["vendor"]
        rows = []
        # get the data from each table 
        for i in tables:
            # the html page has 6 tables but we need only table 3 , 4 and 5 
            num = num+1
            if num == 3 or num == 4 or num == 5:
                # Extract the table headers

                # for th in i.find_all("th"):
                #     headers.append(th.text.strip())

                try:
                    # get table row data
                    for tr in i.find_all("tr")[1:]:
                        try:
                            row = ["Dell"]
                            for td in tr.find_all("td"):
                                row.append(td.text.strip())
                                
                            rows.append(row)
                        except Exception as e:
                            print(f"Could not append row {td}data")
                            print("Error occured")
                except Exception as e:
                    print(f"Could not retrive data for {tr}")
                    print("Error occured ",e)
        # headers[7] = "vendor"

                ###########
                # Convert date format 
        def convert_date(date_str):
            formatted_date = ''
            try:
                # Try to parse the date string as "May 01, 2013" format
                date = datetime.strptime(date_str, '%B %d, %Y')
                formatted_date = date.strftime('%d/%m/%Y')
            except ValueError:
                try:
                    # If it fails, try to parse the date string as "May 2013" format
                    date = datetime.strptime(date_str, '%B %Y')
                    formatted_date = date.strftime('%d/%m/%Y')
                except ValueError:
                    try:
                        date = datetime.strptime(date_str, '%Y')
                        formatted_date = date.strftime('%d/%m/%Y')                
                    except Exception as e:
                        formatted_date = ''
            # Format the date as "dd/mm/yyyy"
        #     formatted_date = date.strftime('%d/%m/%Y')
            return formatted_date

        ##############

        for data in rows:
            try:
                End_of_support = data[6]
                End_of_support = convert_date(End_of_support)
                data[6] = End_of_support
        #         print(End_of_support)

            except Exception as e :
                print(e)


                ##########

        # save the data into Dell_eol_data.csv file 
        with open("Dell_eol_data.csv" , mode="w", newline='') as f:
            csv_writer = csv.writer(f)
            # csv_writer.writerow(headers[7:15])
            for r in rows:
                try:
                    csv_writer.writerow(r)
                except:
                    print(f"Could not write {r}row to csv file ")
                    print("Error occured ",e)
        print("Table data has been saved to Dell_eol_data.csv")

    except Exception as e:
        print("Could not get the data for Dell")
        print("Error occured ", e)



