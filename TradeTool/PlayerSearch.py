from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import csv
import time
import PlayerList


options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


def find_player_url():
    #player_name = input("Input player name, no special characters: ").lower()
    ##player_name = player_name.lower()
    player_name = "Bogdan Bogdanović"
    for player, url in PlayerList.Active_Playerlist.items():
        if player_name in player.lower():
            suffx_url = url.replace(".html", "/gamelog/2024")            
        else:
            print("Player not found")
        full_url = "https://www.basketball-reference.com" + suffx_url
        
    return full_url



def goto_url(full_url):
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    driver.get(full_url)
    html_content = driver.page_source
    print("Found requested Url...")
    return html_content


def save_csv(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    file_path = 'C:\\Users\\abdul\VSProjects\\NBAFantasyTool\\csvData\\PlayerStats.csv'

    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        table = soup.find('table', {'class': 'Table__TBODY'})
        if table:
            for row in table.find_all('tr'):
                data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                writer.writerow(data)
        else:
            print("Table not found")

    print("Data written to CSV file successfully.")

full_url = find_player_url()
html_content = goto_url(full_url)
save_csv(html_content)


