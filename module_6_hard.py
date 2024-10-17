# Задание "Они все так похожи"

import math


class Figure:
    sides_count = 0

    def __init__(self, __color, __sides):
        self.__color = __color  # список цветов (в формате RGB)
        self.__sides = __sides # список сторон (длины)
        #self.filled = filled # закрашенный или нет

    def get_color (self):
        return self.__color

    def __is_valid_color (self, R, G, B):
        ##is_true_1 = False
        #
        #if (R in range (0,255)
        #        and G in range (0,255) and
        #        B in range (0,255)):
        #    is_true_1 = True
        #else:
        #    is_true_1 = False
        #
        return 0<=R<=255 and 0<=G<=255 and 0<=B<=255


    def set_color (self, R, G, B):
        if self.__is_valid_color (R,G,B):
            self.__color = (R,G,B)
        else:
            print ('Ошибка - цвета не в пространстве RGB') # не изменяем цвет !!!

    def __is_valid_sides (self, *args):
        is_true = False
        if len (args) == self.sides_count:
            is_true = True
        else:
            is_true = False
        return is_true

    def get_sides (self):
        return (self.__sides)

    def __len__ (self): # считаем периметр
        perimetr = sum(self.__sides)
        #print (perimetr)
        return perimetr

    def set_sides (self, *new_sides):
        if self.__is_valid_sides (*new_sides):
            self.__sides = new_sides
            print((self.__sides))
        else:
            pass

class Circle (Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        #super().__init__(args[0],args[1])
        super().__init__(color, circumference)
        self.__radius = (round(circumference / (2 * math.pi), 2))

        #if len(args[1])==self.sides_count:
        #    args[1]=[1]*self.sides_count
        #    self.__radius = round(args[1] / (3.14*2),2)
        #    print(f'радиус = {self.__radius}')
        #else:
        #    args[1]=[1]*self.sides_count

    def get_square (self):
        square = round(math.pi * self.__radius**2,2)
        print (f'площадь круга: {square}')

    #def __str__(self):
    #    return f"цвета: {self.__color}, длины сторон: {self.__sides}"

class Triangle (Figure):
    sides_count = 3

    def __init__(self, *args):
        super().__init__(args[0],args[1])

    def get_square (self):
        #p=self.__len__()/2
        #S_2 = p*(p-self._Figure__sides[0])*(p-self._Figure__sides[1])*(p-self._Figure__sides[2]) # квадрат площади
        #self.square = round (S_2 ** (0.5),2)
        a, b, c = self.get_sides()
        p = (a + b + c) / 2  # Полупериметр
        square = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
        print(f'площадь треугольника: {square}')


class Cube (Figure):
    sides_count = 12

    #def __init__(self, *args):
    #    super().__init__(args[0],args[1])
        #new_sides =[self._Figure__sides]*12
        #self._Figure__sides = [self._Figure__sides]*12

    def __init__(self, __color, side_length):
        __sides = [side_length] * 12
        super().__init__(__color, __sides)

    def get_volume (self):
        #self.volume = self._Figure__sides**(3)
        #print(self.volume)
        side = self.get_sides()[0]
        volume = side ** 3
        return f'Объём куба: {volume}'


circle1 = Circle((200, 200, 100),  10) # (Цвет, стороны)
print(circle1.get_sides())

cube1 = Cube((222, 35, 130), 6)
print(cube1.get_sides())

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
circle1.get_square()
print(circle1.get_color())
print(f'длина окружности = {circle1.get_sides()}, радиус = {circle1._Circle__radius}')

triangle1 = Triangle((200, 200, 100),(2,4,5))

triangle1.get_square()

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())

circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(f'длина окружности = {circle1.get_sides()}, радиус = {circle1._Circle__radius}')

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
print(circle1._Circle__radius)


# Проверка объёма (куба):
print(cube1.get_volume())
