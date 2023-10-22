import os

def clean_files():
    # remove processed files
    files = ["microsoft_eol.csv", "IBM_eol_data.csv", "Dell_eol_data.csv", "Adobe_eol_data.csv", "Maria_DB_eol_data.csv", "FreeBSD_eol_data.csv", "Updated_microsoft_eol.xlsx", "microsoft_eol.xlsx" , "cisco_eol_data.csv", "LifecycleMatrix.csv"]
    for file in files:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"{file} file has been removed")
            except Exception as e:
                print(f"Could not remove the {file}")
                print("Error occured ",e)
        else:
            print(F"{file} file does not exist")



