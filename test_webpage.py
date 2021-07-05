#Pupose of the Script
#########################################################################################

#Creating the job and getting the report of it by writing the python code

##########################################################################################
#Below points has been considered in the list.
##########################################################################################
#1.By using python code provide project name, job_name, token.

#2.The token will be generated in integrations and copy it and paste in token.

#3.provide username and password.
###########################################################################################

#Script_name            : test_webpage.py
#Script_Version         : 1.0
#Prepared by            : supriya.jakkamputi@infinite.com
#Create Date            : 4-JUNE-2021
#Last Modification Date : 7-JUNE-2021

#############################################################################################
import logging
from src.testproject.sdk.drivers import webdriver

logging.basicConfig(filename='priya.log',
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)
logging.info("Execution of code starts here")
def simple_test():
    logging.info('Providing the token, name, password for login.')
    driver = webdriver.Chrome(token = 'TBPQ2XC7jwS5rY_fmGv2Z6J2hEYd4aDi3kcKlAnwsWk1')
    
    driver.get("https://example.testproject.io/web/")
    logging.info('providing the web of testproject')
    #Providing username to the web driver
    driver.find_element_by_css_selector("#name").send_keys("supriya")
    logging.info('providing the username')
    #providing password to the web browser.
    driver.find_element_by_css_selector("#password").send_keys("12345")
    logging.info('providing the password')
    #Generate the login. 
    driver.find_element_by_css_selector("#login").click()
    logging.info("login successfully")
    #Execution whether the test is passed or failed
    passed = driver.find_element_by_css_selector("#logout").is_displayed()
    print("Test passed") if passed else print("Test failed")
    driver.quit()

if __name__ == "__main__":
    simple_test()
logging.info('execution of code stops here')
