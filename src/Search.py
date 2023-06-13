from seleniumpagefactory.Pagefactory import PageFactory
import re

class Search(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    
    locators={
        'profileLink':('XPATH','/html/body/p[1]/table[1]/tbody/tr/td[2]/font/b/a')
    }
    
    def get_pid(self):
        pid=self.profileLink.get_attribute("href")
        return pid