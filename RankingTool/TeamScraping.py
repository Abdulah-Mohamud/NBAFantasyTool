from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv






#Function that take URL and webscrap the teams stats into csv

#urls = ["https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=5", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=1", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=9", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=2", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=10", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=3", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=11", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=4", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=12", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=6", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=13", "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=7"]
url= "https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=7"

# def TeamTotals(resource_url):
#     driver = webdriver.Chrome(options=options)
#     driver.get(resource_url)

# TeamTotals(url)

def scrape_and_save_csv(url):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    html = driver.html_content

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    if table:
            # You can further process the table here, for example, print its content
        print(table.prettify())
    else:
        print("No table found on the webpage.")
    print(table)


# # Open a CSV file for writing
#     with open("TeamName", 'w', newline='', encoding='utf-8') as csv_file:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         csv_writer = csv.writer(csv_file)
#         table = soup.find('table', {'class': 'Table Table--align-right Table--fixed Table--fixed-left'})

#         for row in table.find_all('tr'):
#                 row_data = [cell.get_text(strip=True) for cell in row.find_all(['td'])]

#                 # Write the row data to the CSV file
#                 csv_writer.writerow(row_data)
            
#         print(f"Scraping successful. Data saved to {csv_filename}")


# Example usage:
url_to_scrape = 'https://fantasy.espn.com/basketball/team?leagueId=1580336755&teamId=7'
csv_filename = 'scraped_data.csv'  # Choose a filename for the CSV

scrape_and_save_csv(url_to_scrape)
