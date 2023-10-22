import requests
from bs4 import BeautifulSoup
import csv

import urllib3
# to ignore the SSL verification warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://helpx.adobe.com/in/support/programs/eol-matrix.html"
# get the HTML 
# 
def get_adobe_data():
    try: 
        # call the url with get method
        resp = requests.get(url , verify=False)
        # get the html page
        htmlContent = resp.content
        # parse the html page and create Beautiful soup object
        soup = BeautifulSoup(htmlContent , 'html.parser')
        tables = soup.find_all('table')

        # Extract the table headers
   
        # headers = ["vendor"]
        rows = []
        # get tables row and headers
        for i in tables:
          
            # get the table headers
            # for th in i.find_all("th"):
            #     headers.append(th.text.strip())

            # get table row data
            for tr in i.find_all("tr")[1:]:
                row = ["Adobe"]
                for td in tr.find_all("td"):
                    row.append(td.text.strip())

                rows.append(row)

        # save data into csv file 

        with open("Adobe_eol_data.csv" , mode="w", newline='') as f:
            csv_writer = csv.writer(f)
            # csv_writer.writerow(headers[0:7])
            for r in rows:
                csv_writer.writerow(r)
        print("Table data has been saved to Adobe_eol_data.csv")

    except Exception as e:
        print("Could not get the data for Adobe")
        print("Error occured ", e)