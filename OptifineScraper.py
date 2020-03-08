from bs4 import BeautifulSoup
import requests

page = requests.get('https://optifine.net/downloads', auth=('user', 'pass'))
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
