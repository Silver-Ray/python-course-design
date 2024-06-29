import requests
from bs4 import BeautifulSoup


url="https://www.chinanews.com"


request=requests.get(url)

request.encoding='utf-8'

#if request.status_code==200:

