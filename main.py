from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from msvcrt import getch
from getfromplayer import getfromplayer
from getgame import getgame
import os
from alive_progress import alive_bar

def main():
    options = webdriver.ChromeOptions()
    options.add_extension('ext/adblock.crx')
    options.add_argument("--profile-directory=chromeprofile")
    options.add_argument(f"--user-data-dir={os.getcwd()}/chromeprofile".replace("\\","/"))
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options = options)
    
    playerlist = open("playerlist.txt", "r")
    
    for player in playerlist.readlines():
        getfromplayer(player)
    
    print("> Closing driver")
    
    gamelist = open("gamelist.txt", "r").readlines()
    
    with alive_bar(len(gamelist),bar='filling') as bar:
        bar.title("Exporting games to result.pgn")
        for game in gamelist:
            getgame(game)
            bar()
    

if __name__ == "__main__":
    main()