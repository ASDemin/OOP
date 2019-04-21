'''
1. Получите текст из файла.
2. Разбейте текст на предложения.
3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
4. Отберите все ссылки.
5. Ссылки на страницы какого домена встречаются чаще всего?
6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
'''

import re, collections

with open ('text.txt',encoding='utf-8') as file:
    text=file.read()

    dote=re.split('\.', text)

    m_use=[slova for slova in re.split(' ', text )if len(slova)>3]

    pat = re.compile('\w+\.+\w+[.\/+\w+]+\w?')
    links = re.findall(pat, text)

    ch_l = re.sub(pat, 'ссылка будет доступна после регистрации', text)

print(text)
