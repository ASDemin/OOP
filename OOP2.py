'''
1. Создайте классы Noun и Verb.
2. Настройте наследование от Word.
3. Добавьте защищенное свойство «Грамматические характеристики».
4. Перестройте работу метода show класса Sentence.
5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.'''
import re

class Word:

    def __init__(self,text,g_param,part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech
        self.__g_param=g_param

    def get_param(self):
        return self.__g_param

class Noun(Word):
    def __init__(self,text,g_param,part_of_speech = 'noun'):
        super().__init__(text,g_param,part_of_speech)

class Verb(Word):
    def __init__(self,text,g_param,part_of_speech = 'verb'):
        super().__init__(text,g_param, part_of_speech)


class Sentence:

    def __init__(self, contetnt=[], w_list=[]):
        self.content =contetnt
        self.w_list=w_list

    def show(self):
        result =[self.w_list[i].text for i in self.content]
        str_result = " ".join(result)
        return str_result


    def show_parts(self):
        result =[]
        for i in self.content:
            list = self.w_list[i].get_param().split(', ')
            for param in list:
                result.append(param)

#class Sentence:
    #content = [objects for objects in Word]

        result=set(result)
        str_result='Grammar parametres of words in the sentence: {}.'.format(','.join(result))
        return str_result


obj=Sentence([0,1,2],[Noun('Hello','gender, case,role, number'),Noun('my','gender, case,role, number'), Noun('world','gender, case,role, number')])

print (obj.show_parts())
