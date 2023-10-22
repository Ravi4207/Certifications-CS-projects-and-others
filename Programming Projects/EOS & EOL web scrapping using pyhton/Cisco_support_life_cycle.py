import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

def get_cisco_data():
    # URL of the web page containing the table
    urls = {
        "switches" : "https://www.cisco.com/c/en/us/support/switches/index.html#eolanchor",
        "security" : "https://www.cisco.com/c/en/us/support/security/index.html#eolanchor",
        "routers" : "https://www.cisco.com/c/en/us/support/routers/index.html#eolanchor" ,
        "wireless" : "https://www.cisco.com/c/en/us/support/wireless/index.html#eolanchor",
        "unified communications" : "https://www.cisco.com/c/en/us/support/unified-communications/index.html#eolanchor",
        "collaboration endpoints" : "https://www.cisco.com/c/en/us/support/collaboration-endpoints/index.html#eolanchor",
        "cloud system management" : "https://www.cisco.com/c/en/us/support/cloud-systems-management/index.html#eolanchor",
        "conferencing" : "https://www.cisco.com/c/en/us/support/conferencing/index.html#eolanchor",
        "connected-safety-security" : "https://www.cisco.com/c/en/us/support/connected-safety-security/index.html#eolanchor",
        "optical networking" : "https://www.cisco.com/c/en/us/support/optical-networking/index.html#eolanchor",
        
    }
    row_data = []
    
    try:
        for category, url in urls.items():
            try:
                # Send a GET request to the URL
                response = requests.get(url)

                # Parse the HTML content of the web page using BeautifulSoup
                soup = BeautifulSoup(response.content, "html.parser")

                # Find the table element on the page
                # table = soup.find("table", {"class": "dataTable"})
                table = soup.find("table")
                # Extract the data from the table rows
            #     row_data = []
                rows = table.find_all("tr")
                for row in rows:
                    try:
                        # Extract the data from the cells in each row
                        cells = row.find_all("td")
                        r = []
                        for cell in cells:
                            try:
                                if len(cell) > 0:
                                    r.append(cell.text.strip())  

                            except Exception as e:
                                print("Could not retrive row data")
                                print("Error occured ",e)
                        if len(r) > 0:
                            # Remove "\nEOL Details" text from the second element of the list
                            modified_string = r[1].replace('\nEOL Details', '')
                            r[1] = modified_string
                            r.append("Cisco")
                            r.append(category)
                            row_data.append(r)
                #  headers -      end of support date , product , vendor , category
                    except Exception as e:
                        print("Could not retrive data ")
                        print("Erro occured ",e)
            except Exception as e:
                print(f"Could not extract data for this {category} category")
                print("Error occured " , e)        
        # change the end of support date format from "11 Apr 2012" format to "11/04/2012"

        for data in row_data:
            try:
                end_of_support_date = data[0]
                # change end of support date format 
            
                #  parse date string to strptime method and create date object 
                end_of_support_obj = datetime.strptime(end_of_support_date, '%d %b %Y')
                # pasrse date object to strftime method to format the date
                end_of_support_date = end_of_support_obj.strftime('%d/%m/%Y')

                data[0] = end_of_support_date
            except Exception as e:
                print("Could not change the date format for end of support date")
                print("Error occured ",e)

        # save data to csv file 

        with open("cisco_eol_data.csv" , mode="w", newline='') as f:
            csv_writer = csv.writer(f)

            for eol_data in row_data:
                try:
                    csv_writer.writerow(eol_data)
                except Exception as e:
                    print(f"Could not add {eol_data} data to csv file")
                    print("Error  occured ",e)
        print("Table data has been saved to cisco_eol_data.csv")

    except Exception as e:
        print("Could not get the data for Cisco end of support ")
        print("Error occured " , e)