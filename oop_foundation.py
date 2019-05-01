'''
1. Создайте класс Word.
2. Добавьте свойства text и part of speech.
3. Добавьте возможность создавать объект слово со значениями в скобках.
4. Создайте класс Sentence
5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
6. Добавьте метод show, составляющий предложение.
7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.
'''
import re

class Word:
    text = ' '
    part_of_speech = ' '

    def __init__(self,text,part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech

class Sentence:
    content = [i for i in range(1, (len(re.findall('\w+', sentence))+1))]

    def show(self,**sentence):
        for key, value in sentence.items():
            key=list.append(key.text)
            value=list.append(value.text)
        sentence = " ".join(list)
        print(sentence)

    def show_parts(self,**parts):
        for key, value in parts.items():
            key = list.append(key.part_of_speech)
            value = list.append(key.part_of_speech)
        print (list(set1))

f = Word ('Hello','noun')
s = Word ('my','pronoun')
t = Word('is', 'preposition')
f=Word('Alex','noun')
f2=Word('!','sign')

