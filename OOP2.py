'''
1. Создайте классы Noun и Verb.
2. Настройте наследование от Word.
3. Добавьте защищенное свойство «Грамматические характеристики».
'''

from oop_foundation import Word

class Noun(Word):
    type = 'существительное'

class Verb(Word):
    type='глагол'

new = Noun ('new', 'noun')
s_new = Verb ('new','verb')

print(new.type, s_new.part_of_speech)