from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_Vmware_data():

    chrome_op = webdriver.ChromeOptions()
    # set up download directory location
    chrome_op.add_experimental_option("prefs",{"download.default_directory" : "C:\\Users\\spendam\\Downloads\\eol script_updated\\eol script"})

    # # Set up Chrome driver 
    driver = webdriver.Chrome(options=chrome_op)

    # Edge driver 

    # Edge_op = webdriver.EdgeOptions()
    # # # set up download directory location
    # Edge_op.add_experimental_option("prefs",{"download.default_directory" : "C:\\Users\\spendam\\Downloads\\eol script_updated\\eol script"})

    # # Set up Edge driver 
    # driver = webdriver.Edge(options=Edge_op)

    # driver = webdriver.Chrome()
    # Navigate to VMware Lifecycle product matrix page
    driver.get('https://lifecycle.vmware.com/#')

    # Wait for the button to be clickable and click it
    try:
        # select the Unsupported checkbox in website 
        Unsupported_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='step2']/label")))
        time.sleep(5)
        Unsupported_button.click()
        time.sleep(10)
        print("Unsupported has been selected")
        # click the Download csv icon 
        csv_button = WebDriverWait(driver, 18).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='step4']"))
        )
        csv_button.click()
        print("file has been downloaded")
    except:
        print("Step 4 button not found")

    time.sleep(10)
        # Close the browser


    driver.quit()