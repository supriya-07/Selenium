#Importing the modules
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Created a class for webpage
class DuckDuckGoSearchPage:
  
  URL = 'https://www.duckduckgo.com'
  SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

  
  def __init__(self, browser):
    self.browser = browser

  #Loading the Url
  def load(self):
    self.browser.get(self.URL)

  #Performing search operation
  def search(self, phrase):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase + Keys
