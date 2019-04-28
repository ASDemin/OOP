'''
1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.
'''

import requests, json

def iata(a):
    link = 'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20'+a+'%20в%20Лондон'
    data=json.loads(requests.get(link).text)
    return  data['origin']['iata']

print(iata(input('Введите название города')))