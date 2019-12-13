# import requests
# from bs4 import BeautifulSoup
# # from requests.packages.urllib3.exceptions import InsecureRequestWarning
# # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# r = requests.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=18015743')  # , verify=False

# bs = BeautifulSoup(r.text, 'lxml')  # html.parser, lxml (lxml이 성능면에 좋음)

# print(bs.select('#ifrCalendar #CellPlayDate0'))

# # lists = bs.find_all('li', {'class': 'ah_item'})

# # for li in lists:
# #     print(li)

from selenium import webdriver
from bs4 import BeautifulSoup
import telepot
from datetime import datetime
import time

token = '1053803038:AAF9dDYMwoBUm99QExm9nzgh5YoDm1UYAlQ'
mc = '1018410037'
# '962521655'

bot = telepot.Bot(token)

# bot.sendMessage(mc, '안녕하세요. 정해성입니다.')

path = 'E:\\study\\python\\python_study\\09.크롤링\\chromedriver.exe'

#
users = ('962521655', '1018410037')

days = {
    '1': '1박2일',
    '2': '2박3일'
}

products = {
    '1': '시민가족캠핑존구역',
    '2': '오토캠핑존',
    '3': '카라반A',
    '4': '카라반B'
}

print('################### 프로그램 시작 ###################')
print()
print('★ tip 여러 항목 선택시 띄어쓰기로 구분합니다.')
print()

use_date = input('이용일자를 입력하세요. ex) 20191224 20191225 20191226 : ').split(' ')
print('이용일자 : ', use_date)
print()

use_day = input('이용박수를 선택하세요. (1: 1박2일, 2: 2박3일) : ').split(' ')

print()
print('이용박수')
for i in use_day:
    print(days.get(i), end=' ')

print()
use_products = input('이용상품을 선택하세요. (1: 시민가족캠핑존구역, 2: 오토캠핑존, 3: 카라반A, 4: 카라반B) : ').split(' ')

print()
print('이용상품')
for i in use_products:
    print(products.get(i), end=' ')

print()
print()

driver = webdriver.Chrome(path)
driver.implicitly_wait(3)
driver.get("http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=18015743")

print('브라우저 로드 완료')

def changeMonth(YYYYMM):
    driver.switch_to_frame('ifrCalendar')
    time.sleep(0.5)
    driver.execute_script("fnChangeMonth('{}')".format(YYYYMM))

def changeDate(DD):
    driver.switch_to_default_content()
    time.sleep(0.5)
    driver.execute_script("$('#ifrCalendar').contents().find('a:contains(\"{}\")').trigger('click')".format(DD))

#####

cur_month = datetime.today().strftime("%Y%m")
changeMonth(cur_month)

for i in use_date:

    print('사용일자 : ', i, i[0:6])

    if cur_month != i[0:6]:
        cur_month = i[0:6]
        changeMonth(cur_month)
    
    print('사용일 : ', i[6:8])
    changeDate(i[6:8])

    for j in use_day:

        print('이용박수 : ', j)

        time.sleep(0.5)
        driver.execute_script("$('ul#ulPlaySeq li:eq({}) label').trigger('click')".format(j))

        time.sleep(0.5)
        html = driver.page_source

        bs = BeautifulSoup(html, 'lxml')
        ele_products = bs.select('#ulSeatList>li')

        print('상품목록 : ', ele_products)

        product_msg = ''

        for idx, product in enumerate(ele_products):
            if str(idx + 1) in use_products:
                print('상품재고 : ', product.text.split(' ')[1])
                if product.text.split(' ')[1] != '매진':
                    product_msg += product.text + '\n'

        for k in users:
            bot.sendMessage(k, i + '\n' + product_msg)







# 1, 2, 3, 4 (1: 시민가족캠핑존구역, 2: 오토캠핑존, 3: 카라반A, 4: 카라반B)
# time.sleep(0.5)
# html = driver.page_source

# bs = BeautifulSoup(html, 'lxml')
# ele_products = bs.select('#ulSeatList>li')

# a = ''

# for idx, product in enumerate(ele_products):
#     print(idx, product.text)
#     # if idx 

#     if a in ele_products:
#         print()

# # 도리 : 1018410037