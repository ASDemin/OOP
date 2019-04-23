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

    m_use=collections.Counter([slova for slova in re.split(' ', text )if len(slova)>3]).most_common(1)

    pat = re.compile('\w+\.+\w+[.\/+\w+]+\w?')

    links = re.findall(pat, text)

    m_domain=" ".join(links)
    m_domain=(re.split('\.',re.sub('\/+\w+',' ',m_domain)))
    m_domain=collections.Counter([slova for slova in m_domain if len(slova)>3]).most_common(1)

    ch_l = re.sub(pat, 'ссылка будет доступна после регистрации', text)

print(m_domain)
