import requests
from bs4 import BeautifulSoup
import csv

file = open('gtorr.csv', 'w', encoding='utf-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['წელი', 'სახელი'])

for i in range(2,7):
    url = f'https://gtorr.net/index.php?cstart={i}&do=cat&category=shooter'
    r = requests.get(url, timeout=(15, 20))
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find("div", class_='content-block')

    games = div.find_all('div', class_='main-news')

    for game in games:
        yr = game.find('span', {'style': 'font-family: Fira Sans;'})
        year = yr.text

        game_titl = game.find('div', class_='main-news-title')
        title = game_titl.a.text
        file.write(year + ',' + title + "," + '\n')





file.close()
