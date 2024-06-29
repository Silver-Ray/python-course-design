import requests
from bs4 import BeautifulSoup

url='https://www.chinanews.com/scroll-news/news1.html'

response=requests.get(url)
if response.status_code==200:
    response.encoding='utf-8'

soup=BeautifulSoup(response.text,'html.parser')

content_list=soup.find('div',{'class':'content_list'})
li_list=content_list.find_all('li',{'class':None})
for li in li_list:

print()