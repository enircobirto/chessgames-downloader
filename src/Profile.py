from seleniumpagefactory.Pagefactory import PageFactory
import re

class Profile(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    
    locators={
        'pageCount':('XPATH','/html/body/font[2]/table[2]/tbody/tr/td[1]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[1]/font')
    }
    
    def get_page_count(self):
        return int(re.findall(r'of (.*?);',self.pageCount.get_text())[0])