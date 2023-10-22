import requests
import openpyxl
import json
import urllib3
import pandas as pd
import csv
# to ignore the SSL verification warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_IBM_data():
    try:
        
        header = {
            'Accept-Encoding': 'gzip'
                }
        payload = {}
        url = "https://www.ibm.com/support/pages/sites/default/files/software-lifecycle/ibm_software_lifecycle_product_list.csv"
        # returns csv file
        resp = requests.get(url , headers=header , data=payload , verify=False)
       
        # save the data into csv file 
        f = open('IBM_eol_data.csv', "w" ,encoding="utf-8")
        f.writelines(resp.text)
        f.close()
        

        # change the first header name 

        # Open the CSV file in read mode
        with open('IBM_eol_data.csv', 'r' , encoding="utf-8") as file:

            # Read the CSV file into a list of rows
            rows = list(csv.reader(file))

            # Change the first header name 
            rows[0][0] = 'Product'

        # Open the CSV file in write mode and write the updated rows
        with open('IBM_eol_data.csv', 'w', newline='' , encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("first header data has been changed")

        # get the column 1 size       
        filename = 'IBM_eol_data.csv'
        column_name = 'Product'

        # Open the CSV file for reading
        with open(filename, 'r' , encoding="utf-8") as csvfile:
            # Create a reader object using the csv module
            reader = csv.DictReader(csvfile)
            
            # Initialize a list to hold the values in the column
            column_values = []
            
            # Iterate over each row in the CSV file
            for row in reader:
                # Append the value in the specified column to the list
                column_values.append(row[column_name])
            
            # Get the length of the list to determine the size of the column
            column_size = len(column_values)+1

        # Print the size of the column
        print(f'The size of column {column_name} is {column_size}.')

        # add vendor column to csv file 
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv('IBM_eol_data.csv')

        # Define the new column as a list
        new_column = []

        for i in range(1 , column_size):
            new_column.append("IBM")

        # Add the new column to the DataFrame
        df['vendor'] = new_column

        # Write the updated DataFrame to a new CSV file
        df.to_csv('IBM_eol_data.csv', index=False)
        print("Vendor column has been added")
        print("Data has been saved in IBM_eol_data.csv file")
        # Open the CSV file in read mode
        # remove the headers from csv file
        with open('IBM_eol_data.csv', 'r' , encoding="utf-8") as file:

            # Read the CSV file into a list of rows
            rows = list(csv.reader(file))

            # remove first index from the list that contains headers
            rows.pop(0)

        # Open the CSV file in write mode and write the updated rows
        with open('IBM_eol_data.csv', 'w', newline='' , encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
      

    except Exception as e:
        print("Could not get the data for IBM ")
        print("Error occured ",e)


