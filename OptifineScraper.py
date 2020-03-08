from bs4 import BeautifulSoup
import requests
import re
import time

page = requests.get('https://optifine.net/downloads')
print('got downloads')
#page = requests.get('https://optifine.net/changelog?f=preview_OptiFine_1.15.2_HD_U_G1_pre9.jar', auth=('user', 'pass'))
#print ('got changelog')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
print('Getting changelog')
link = soup.find(text='OptiFine 1.15.2 HD U G1 pre9').findNext('td',class_='downloadLineChangelog').findNext('a')
if link.has_attr('href'):
        address='https://optifine.net/'+link['href']
        page=requests.get(address)

print('Change log obtained')
soup=BeautifulSoup(page.content,'html.parser')
print(str(soup))

m=re.search('C[a-zA-Z][a-zA-Z]',str(soup))
#m=re.search('Optifine 1.15.2[.]*/([0-3][0-9]-[0-1][0-9]-2020)',str(soup))
print(m.group(1))

