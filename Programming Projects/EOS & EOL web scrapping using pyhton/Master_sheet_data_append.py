import pandas as pd
import csv 
from datetime import datetime

def append_data_master_sheet():
    try:
        # add headers to csv file
        with open('Master_EOL_data.csv' , mode="w", newline='') as f:
            csv_writer = csv.writer(f)
            # header length = 8
            headers = ["Product" , "Release" ,"ExtendedEndDate", "End of life"  ,"Vendor" , "End of support" , "Branch" , "Status"] 
            csv_writer.writerow(headers)
            print("Headers have been added to master csv file")
    except Exception as e:
        print("Could not create new csv file ")
        print("Error occured ", e)
    ##########
    try:
        # append microsoft data into master sheet csv file
        # Open the source CSV file
        with open('microsoft_eol.csv', 'r' ) as source_file:
            source_csv_reader = csv.reader(source_file)
            csv_reader = list(source_csv_reader)

            # Open the destination CSV file
            with open('Master_EOL_data.csv', 'a',newline='' ) as dest_file:
                dest_csv_writer = csv.writer(dest_file)

                # Loop through the rows of the source CSV file
                for row in csv_reader[2:]:
                    # remove "00:00:00" text from the date
                    ExtendedEndDate = row[6]
                    if "00:00:00" in ExtendedEndDate:
                        ExtendedEndDate = ExtendedEndDate.replace(" 00:00:00", "")
                        
                    # remove "00:00:00" text from the date
                    End_of_life = row[7]
                    if "00:00:00" in End_of_life:
                        End_of_life = End_of_life.replace(" 00:00:00", "")
                    
    #["Product" , "Release" ,"ExtendedEndDate", "End of life" ,"Vendor" , "End of support" ,  "Branch" , "Status"]               
                    # Append the values from columns Product , VRM ,'' , '' ,vendor ,end of support date  to the new row
                    new_row = [row[0], row[2],ExtendedEndDate,End_of_life, row[11],'','','']

                    # Write the new row to the destination CSV file
                    dest_csv_writer.writerow(new_row)
        print("microsoft data has been appended to master sheet")
    except Exception as e:
        print("Could not append microsoft data into master sheet csv file")
        print("Error occured ", e )
############

    ############

    try:
        # append IBM data into master sheet csv file
            # open IBM csv file to read the data
        with open('IBM_eol_data.csv', 'r' ,  encoding="utf-8") as source_file:
            source_csv_reader = csv.reader(source_file)

            # Open the Master CSV file to append the data
            with open('Master_EOL_data.csv', 'a', newline = '') as dest_file:
                dest_csv_writer = csv.writer(dest_file)

                # Loop through the rows of the IBM_eol_data CSV file
                for row in source_csv_reader:
                    #"Product" , "Release" ,"ExtendedEndDate", "End of life"  ,"Vendor" , "End of support" , "Branch" , "Status"               
                    # Append the values from columns Product , VRM ,'' , '' ,vendor ,end of support date  to the new row
                    new_row = [row[0], row[1],'', '',row[16] , row[8], '','']

                    # Write the new row to the Master_EOL_data CSV file
                    dest_csv_writer.writerow(new_row)
        print("IBM data has been appended to master sheet")
    except Exception as e:
        print("Could not append IBM data into master sheet csv file")
        print("Error occured ", e )

    #########
    try:
        # append Dell data into master sheet csv file
        # Open the Dell_eol_data.csv file
        with open('Dell_eol_data.csv', 'r' ) as source_file:
            source_csv_reader = csv.reader(source_file)

            # Open the Master_EOL_data.csv file
            with open('Master_EOL_data.csv', 'a', newline='') as dest_file:
                dest_csv_writer = csv.writer(dest_file)

                # Loop through the rows of the Dell_eol_data.csv file
                for row in source_csv_reader:
                    # master sheet headers
                    #"Product" , "Release" ,"ExtendedEndDate", "End of life"  ,"Vendor" , "End of support" , "Branch" , "Status"  
                    # Append the values from columns Product Name , Release family , '',Vendor , end of support,'','' to the new row
                    new_row = [row[1], row[2],'','', row[0] , row[6],'','']

                    # Write the new row to the Master_EOL_data.csv file
                    dest_csv_writer.writerow(new_row)
        print("Dell data has been appended to master sheet")
    except Exception as e:
        print("Could not append Dell data into master sheet csv file")
        print("Error occured ",e)
    ###########

    # # append Adobe data into master sheet csv file

    try:
        # Open the Adobe_eol_data.csv file
        with open('Adobe_eol_data.csv', 'r' ) as source_file:
            source_csv_reader = csv.reader(source_file)

            # Open the Master_EOL_data.csv file
            with open('Master_EOL_data.csv', 'a',newline='' ) as dest_file:
                dest_csv_writer = csv.writer(dest_file)

                # Loop through the rows of the Adobe_eol_data.csv file
                for row in source_csv_reader:
                    extended_date = row[6]
                    end_of_support = row[5]
                    # change extended date format
                    try:
                        if len(extended_date) < 11:
                            # 
                            if "N/A" in extended_date or "NA" in extended_date:
                                extended_date = ''
                            else:
                                # convert date in dd/mm/yy format
                                # if date contains * char then remove it
                                if "*" in extended_date:
                                    extended_date = extended_date.removesuffix("*")
                                    if "/" in extended_date:
                                        extended_date = datetime.strptime(extended_date, "%m/%d/%Y").strftime("%d-%m-%y")
                                    else:
                                        extended_date = datetime.strptime(extended_date, "%m-%d-%Y").strftime("%d/%m/%y")

                                if "/" in extended_date:
                                    extended_date = datetime.strptime(extended_date, "%m/%d/%Y").strftime("%d-%m-%y")
                                else:
                                    extended_date = datetime.strptime(extended_date, "%m-%d-%Y").strftime("%d/%m/%y")
                        # if its not date format then assign string
                        else:
                            extended_date = ''
                    except Exception as e:
                        print(f"Could not convert date format for extended date {extended_date}")
                        print("Error occured ", e)
                    # change end of support format
                    try:
                        if len(end_of_support) < 11:
                            if "N/A" in end_of_support or "NA" in end_of_support:
                                end_of_support = ''
                            else:
                                # if date contains * char then remove it
                                if "*" in end_of_support:
                                    end_of_support = end_of_support.removesuffix('*')
                                    if "/" in end_of_support:
                                        end_of_support = datetime.strptime(end_of_support, "%m/%d/%Y").strftime("%d/%m/%y")
                                    else:
                                        end_of_support = datetime.strptime(end_of_support, "%m-%d-%Y").strftime("%d/%m/%y")

                                if "/" in end_of_support:
                                    end_of_support = datetime.strptime(end_of_support, "%m/%d/%Y").strftime("%d/%m/%y")
                                else:
                                    end_of_support = datetime.strptime(end_of_support, "%m-%d-%Y").strftime("%d/%m/%y")
                        else:
                            end_of_support = ''
                    except Exception as e:
                        print(f"Could not convert date format for end of support {end_of_support}")
                        print("Error occured " , e)
    # Headers
    #"Product" , "Release" ,"ExtendedEndDate", "End of life"  ,"Vendor" , "End of support" , "Branch" , "Status"   
    # Append the values from columns Product Name, Version, end of extended support,'',Vendor,end of support ,'','' to the new row
                    new_row = [row[1], row[2],extended_date,'', row[0] ,end_of_support,'','']

                    # Write the new row to the Master_EOL_data.csv CSV file
                    dest_csv_writer.writerow(new_row)
        print("Adobe data has been appended to master sheet ")
    except Exception as e:
        print("Could not append Adobe data into master sheet csv file")
        print("Error occured ", e)
    ###########

    #########
    try:
        # append MariaDB data into master sheet csv file
        # Open the Maria_DB_eol_data.csv file
        with open('Maria_DB_eol_data.csv', 'r' ) as source_file:
            source_csv_reader = csv.reader(source_file)

            # Open the Master_EOL_data.csv file
            with open('Master_EOL_data.csv', 'a',newline='' ) as dest_file:
                dest_csv_writer = csv.writer(dest_file)

                # Loop through the rows of the source CSV file
                for row in source_csv_reader:
     #"Product" , "Release" ,"ExtendedEndDate", "End of life"  ,"Vendor" , "End of support" , "Branch" , "Status"  
                    # Append the values from columns Product , Release series , '',end of life,Vendor ,'' ,'','' to the new row
                    new_row = [row[1], row[2],'',row[4], row[0] ,'','','']

                    # Write the new row to the Master_EOL_data.csv file
                    dest_csv_writer.writerow(new_row)
        print("MariaDB data has been appended to master sheet")
    except Exception as e:
        print("Could not append MariaDB data into master sheet csv file")
        print("Error occured ",e)
    ###########

    #########
    try:
        # append FreeBSD data into master sheet csv file
        # Open the FreeBSD_eol_data.csv file
        with open('FreeBSD_eol_data.csv', 'r' ) as source_file:
            source_csv_reader = csv.reader(source_file)

            # Open the Master_EOL_data.csv file
            with open('Master_EOL_data.csv', 'a',newline='' ) as dest_file:
                dest_csv_writer = csv.writer(dest_file)

                # Loop through the rows of the FreeBSD_eol_data.csv file
                for row in source_csv_reader:
    #"Product" , "Release" ,"ExtendedEndDate", "End of life"  ,"Vendor" , "End of support" , "Branch" , "Status"
                    # Append the values from columns Product , Release , '',end of life ,Vendor ,'' ,Branch, '' to the new row
                    new_row = [row[0], row[2],'',row[4], row[0] ,'', row[1],'']

                    # Write the new row to the Master_EOL_data.csv file
                    dest_csv_writer.writerow(new_row)
        print("FreeBSD data has been appended to master sheet")
    except Exception as e:
        print("Could not append FreeBSD data into master sheet csv file")
        print("Error occured ",e)
    ###########