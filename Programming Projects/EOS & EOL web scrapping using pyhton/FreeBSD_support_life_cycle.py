import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import urllib3
# to ignore the SSL verification warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_FreeBSD_data():

    try:
        url = "https://www.freebsd.org/security/#sup"
        # get the HTML page content
        resp = requests.get(url , verify=False)
        htmlContent = resp.content

        soup = BeautifulSoup(htmlContent , 'html.parser')
        tables = soup.find_all('table')

        # Extract the table headers

        # headers = ["Vendor" , "Branch" , "Release" , "Release Date" , "Expected eol"]
        rows = []
        for i in tables:
            # get the table headers
            # for th in i.find_all("th"):
            #     headers.append(th.text.strip())

            # get table row
            for tr in i.find_all("tr")[1:]:
                row = ["FreeBSD"] # add vendor name to list
                # get the table data from row
                for td in tr.find_all("td"):
                    row.append(td.text.strip())

                rows.append(row)

        # change the Release date and expected end of life date format from "September 30, 2026" format to "30/09/2026"
        try:
            for data in rows:
                try:
                    Release_Date = data[3]
                    # change Release date format 
                    if len(Release_Date) < 19:
                        if "n/a" in Release_Date:
                            Release_Date = ''
                        else:                                                
                            # create date object 
                            Release_obj = datetime.strptime(Release_Date, "%B %d, %Y")
                            # pasrse date object to strftime method to format the date
                            Release_Date = Release_obj.strftime("%d/%m/%Y")
                    else:
                        Release_Date = ''
                    data[3] = Release_Date
                except Exception as e:
                    print("Could not change the date format for Release Date")
                    print("Error occured ",e)

                try:
                    Expected_eol = data[4]
                    # change expected end of life date format
                    # if string length is greater than 11 that means it is not a date
                    if len(Expected_eol) < 19:
                        if "n/a" in Expected_eol:
                            Expected_eol = ''
                        else:                        
                            # create date object 
                            Expected_eol_obj = datetime.strptime(Expected_eol, '%B %d, %Y')
                            # pasrse date object to strftime method to format the date
                            Expected_eol = Expected_eol_obj.strftime('%d/%m/%Y')
                    else:
                        Expected_eol = ''
                    data[4] = Expected_eol
                except Exception as e:
                    print("Could not change the date format for expected end of life Date")
                    print("Error occured ",e)
            
        except Exception as e:
            print("Could not change the date format for release date and expected end of life")
            print("Error occured ", e)

        # save data to csv file 

        with open("FreeBSD_eol_data.csv" , mode="w", newline='') as f:
            csv_writer = csv.writer(f)
            # csv_writer.writerow(headers[0:5])
            for r in rows:
                csv_writer.writerow(r)
        print("Table data has been saved to FreeBSD_eol_data.csv")
    except Exception as e:
        print("Could not get the data for FreeBSD")
        print("Error occured ",e )