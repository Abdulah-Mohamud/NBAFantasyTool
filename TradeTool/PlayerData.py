from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(options=options)

url = "https://www.basketball-reference.com/players/s/sabondo01/gamelog/2024"

print("Navigating to URL...")
driver.get(url)

html_content = driver.page_source
driver.quit()

soup = BeautifulSoup(html_content, "html.parser")

file_path = 'C:\\Users\\abdul\\VSProjects\\NBATradeCalc\\csvData\\PlayerStats.csv'

with open(file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    table = soup.find('table', {'id': 'pgl_basic'})
    if table:
        for row in table.find_all('tr'):
            data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
            writer.writerow(data)
    else:
        print("Table not found")

print("Data written to CSV file successfully.")