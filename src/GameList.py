from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
import re

class GameList(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    
    locators={
        'table':('XPATH','/html/body/p[2]/table[1]'),
        'pageCount':('XPATH','/html/body/p[2]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[1]/font')
    }
    
    def get_page_count(self):
        return int(re.findall(r'of (.*?);',self.pageCount.get_text())[0])
    
    def get_game_list(self):
        links = self.table.find_elements(By.TAG_NAME,"a")
        for link in links:
            gamelist = open("gamelist.txt","a")
            href=link.get_attribute("href")
            if "chessgame?gid=" in href and "&comp" not in href:
                gamelist.write(str(href)+"\n")
            gamelist.close()