from msvcrt import getch
from seleniumpagefactory.Pagefactory import PageFactory

class Home(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    
    locators={
        'searchInput':('XPATH','//*[@id="cg-search"]/div/form/input[1]'),
        'searchButton':('XPATH','//*[@id="cg-search"]/div/form/input[2]')
    }
    
    def type_player(self,text):
        self.searchInput.set_text(text+'\n')
    def search(self):
        self.searchButton.click()