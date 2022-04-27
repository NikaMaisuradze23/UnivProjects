import requests
from bs4 import BeautifulSoup
file = open('result.csv', 'w', encoding='utf-8_sig')

url = 'https://www.lit.ge/index.php?page=books&send[shop.catalog][order]=1&send[shop.catalog][reset]=1'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

section = soup.find("section", class_='list-holder')

books = section.find_all('article')
file.write('სათარუი' + "," + 'ავტორუი' + "," + 'ფასი')
for book in books:
    title_bar = book.find('div', class_='title-bar')
    book_name = title_bar.a.text
    author = title_bar.b.a.text
    price = book.button.text.strip()
    file.write(book_name + ',' + author + "," + price + '\n')

file.close()