import pandas as pd
import csv 
from datetime import datetime

def HW_data_append():

    try:
        # add headers to csv file
        with open('HW_Master_Data.csv' , mode="w", newline='') as f:
            csv_writer = csv.writer(f)
            headers = ["Product Release" , "Support Status" ,"General Availability", "End of General Support" ,"End of Technical Guidance" , "End of Availability" ,  "Category" , "Vendor"]
            csv_writer.writerow(headers)
            print("Headers have been added to HW master csv file")
    except Exception as e:
        print("Could not create new csv file ")
        print("Error occured ", e)
    ##########
    ############

    #########
    try:
        # append VMware data into master sheet csv file
        # Open the source CSV file
        with open('LifecycleMatrix.csv', 'r' ,encoding="utf-8") as source_file:
            csv_data = csv.reader(source_file)
            source_csv_reader = list(csv_data)

            # Open the destination CSV file
            with open('HW_Master_Data.csv', 'a',newline='',encoding="utf-8" ) as dest_file:
                dest_csv_writer = csv.writer(dest_file)
                        
                # Loop through the rows of the source CSV file
                for row in source_csv_reader[1:]:
                    if len(row) > 1 :
                        Product_Release = row[0] 
                        End_Technical_Guidance = row[4]
                        if "N/A" in End_Technical_Guidance:
                            End_Technical_Guidance = ''
                        if len(Product_Release) > 90 or "NOTES:" in Product_Release:
                            continue
                    
    #"Product Release" , "Support Status" ,"General Availability", "End of General Support" ,"End of Technical Guidance" , "End of Availability" ,  "Category" , "Vendor" 
    # Append the values from columns  to the new row
                        Vendor = "Vmware"
                        new_row = [Product_Release, row[1], row[2],row[3],End_Technical_Guidance,row[5] ,'' ,Vendor ]

                    # Write the new row to the destination CSV file
                        dest_csv_writer.writerow(new_row)
        print("VMware data has been appended to master sheet")
    except Exception as e:
        print("Could not append VMware data into HW master sheet csv file")
        print("Error occured ",e)
    ###########

    #########
    try:
        # append Cisco data into master sheet csv file
        # Open the source CSV file
        with open('cisco_eol_data.csv', 'r' ) as source_file:
            csv_data = csv.reader(source_file)
            source_csv_reader = list(csv_data)

            # Open the destination CSV file
            with open('HW_Master_Data.csv', 'a',newline='' ) as dest_file:
                dest_csv_writer = csv.writer(dest_file)

                # Loop through the rows of the source CSV file
                for row in source_csv_reader:
    #"Product Release" , "Support Status" ,"General Availability", "End of General Support" ,"End of Technical Guidance" , "End of Availability" ,  "Category" , "Vendor"
                    # Append the values from columns End of support date,Product,Vendor,Category to the new row
                    new_row = [row[1],'','',row[0], '','',row[3], row[2]]

                    # Write the new row to the destination CSV file
                    dest_csv_writer.writerow(new_row)
        print("Cisco data has been appended to master sheet")
    except Exception as e:
        print("Could not append Cisco data into master sheet csv file")
        print("Error occured ",e)
    ###########