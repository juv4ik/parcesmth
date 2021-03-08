# парсинг diy by
import requests
from lxml import html

url = 'https://diy.by/catalog/instrument_and_electrical/976.html?PAGECOUNT=80&FIRSTLEVID=instrument_and_electrical&CATSECT=976&PAGEN_1=1'
response = requests.get(url = url)
print(response.status_code)
tree = html.fromstring(response.text)
print(response.text)
