import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

r = requests.get('https://www.naver.com', verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
lists = bs.find_all('li', {'class': 'ah_item'})

# print(lists)

for li in lists:
    print(li)