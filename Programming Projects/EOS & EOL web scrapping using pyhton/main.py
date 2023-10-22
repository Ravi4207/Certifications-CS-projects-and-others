import threading
import os
import Adobe_support_life_cycle
import Dell_support_life_cycle
import IBM_support_life_cycle
import Microsoft_support_life_cycle
import Master_sheet_data_append
import Cisco_support_life_cycle
import FreeBSD_support_life_cycle
import Maria_DB_support_life_cycle
import Clean_files
import VMware_support_life_cycle
import HW_master_data_append
# call the vendor functions to get the data and save to csv or excel file
# get Adobe vendor data
'''
print("trying to get the data for Adobe..")
Adobe_support_life_cycle.get_adobe_data()
# get Dell vendor data
print("trying to get the data for Dell..")
Dell_support_life_cycle.get_dell_data()
# get IBM vendor data
print("trying to get the data for IBM..")
IBM_support_life_cycle.get_IBM_data()
# get Microsoft vendor data
print("trying to get the data for Microsoft..")
Microsoft_support_life_cycle.get_microsoft_data()

# get FreeBSD vendor data
print("trying to get the data for FreeBSD..")
FreeBSD_support_life_cycle.get_FreeBSD_data()

# get MariaDB vendor data
print("trying to get the data for MariaDB..")
Maria_DB_support_life_cycle.get_MariaDB_data()

# get Cisco vendor hardware data
print("trying to get the data for Cisco..")
Cisco_support_life_cycle.get_cisco_data()

# append all vendors data in one Master sheet csv file 
print("trying to append all vendors data to master sheet")
Master_sheet_data_append.append_data_master_sheet()'''

if __name__ == "__main__":
    # creating threads
    t1 = threading.Thread(target=Adobe_support_life_cycle.get_adobe_data(), name='t1')
    t2 = threading.Thread(target=Dell_support_life_cycle.get_dell_data(), name='t2')
    t3 = threading.Thread(target=IBM_support_life_cycle.get_IBM_data(), name='t3')
    t4 = threading.Thread(target=Microsoft_support_life_cycle.get_microsoft_data(), name='t4')
    t5 = threading.Thread(target=FreeBSD_support_life_cycle.get_FreeBSD_data(), name='t5')
    t6 = threading.Thread(target=Maria_DB_support_life_cycle.get_MariaDB_data(), name='t6')
    t7 = threading.Thread(target=Cisco_support_life_cycle.get_cisco_data(), name='t7')
    t8 = threading.Thread(target=VMware_support_life_cycle.get_Vmware_data(), name='t8')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    if not (t1.is_alive() and t2.is_alive() and t2.is_alive() and t3.is_alive() and t4.is_alive() and t5.is_alive() and t6.is_alive() and t7.is_alive() and t8.is_alive()):
        Master_sheet_data_append.append_data_master_sheet()
        HW_master_data_append.HW_data_append()
        # remove processed files 
        Clean_files.clean_files()
        print("Done")


print("completed")



