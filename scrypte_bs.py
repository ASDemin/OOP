'''
1. Получить количество учеников с сайта geekbrains.ru:
a) при помощи регулярных выражений,
b) при помощи библиотеки BeautifulSoup.
'''

from bs4 import BeautifulSoup as BS

with open('index.html',encoding='utf-8') as f:
    s = f.read()

soup=BS(s,'html.parser')

li=soup.find_all('span')
for i in li:
    print (i.string)