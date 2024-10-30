
#Функциональное разнообразие

from os import write
#import random

#Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

my_func_1 =  map (lambda x,y: x==y,  first, second)
print(list(my_func_1))

#Замыкание:

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file=open(file_name,'w')

        for data in data_set:
            file.write(str(data)+"\n")
            #file.write(f'{data} \n')
        file.close()

    return write_everything


write = get_advanced_writer ('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice (self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())