'''
1. Получить количество учеников с сайта geekbrains.ru:
a) при помощи регулярных выражений,
b) при помощи библиотеки BeautifulSoup.
'''

import re

with open('index.html',encoding='utf-8') as f:
    s = f.read()

print(re.findall('<span class="total-users">Нас уже ([\w ]+) человек<\/span>',s ))



