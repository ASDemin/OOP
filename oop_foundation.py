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

    def __init__(self,text,part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech


class Sentence:

    def __init__(self, contetnt=[], w_list=[]):
        self.content =contetnt
        self.w_list=w_list

    def show(self):
        result =[self.w_list[i].text for i in self.content]
        str_result = " ".join(result)
        return str_result

    def show_parts(self):
        result =[self.w_list[i].part_of_speech for i in self.content]
        result=set(result)
        str_result='In the sentence use {}.'.format(','.join(result))
        return str_result


obj=Sentence([0,1,2],[Word('Hello','noun'),Word('my','noun'), Word('world','noun')])
print(obj.show())
print (obj.show_parts())
