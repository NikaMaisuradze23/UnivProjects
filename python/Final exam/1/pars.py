import requests
from bs4 import BeautifulSoup
import csv

file = open('Uni.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['University'])

file = open('sample.html')
soup = BeautifulSoup(file, 'html.parser')
div = soup.find("nav", class_='column')
uni = div.find('ul')
result = uni.text
print(result)
# file.write(result)

#სურათის წამოღება
div_img = soup.find("div", {'id':'footer-wrapper'})
img = div_img.find('img')
img_url = img['src']

res_img = requests.get(img_url)
img_file = open('google.png', 'wb')
img_file.write(res_img.content)
img_file.close()

file.close()