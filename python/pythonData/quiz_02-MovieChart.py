

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

url = 'https"//www.moviechart.co.kr/rank/boxoffice'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

infos = soup.findAll('div', attrs = {'class': 'listTable group1'})
# print('-' * 50)
# print(infos)
# print('-' * 50)

mydata0 = [i for i in range(1,20)]

