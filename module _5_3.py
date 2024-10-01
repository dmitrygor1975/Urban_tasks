# Модуль 5.3 Задача " Перегрузка операторов":

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floor = number_of_floors

    def go_to (self, new_floor):

        if new_floor > self.number_of_floor or new_floor < 1:
            print("Такого этажа не существует")


        else:
            root_house =list(range(1,new_floor+1))
            print(root_house)

    def __len__(self):
        #print(f"количество этажей: {self.number_of_floor}")
        return self.number_of_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

        elif isinstance(other, int):
            return self.number_of_floor == other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor > other

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor >= other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor < other

    def __le__(self, other):
        if isinstance(other, House) :
            return self.number_of_floor <= other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor <= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor != other

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floor += other.number_of_floor
            return self
        elif isinstance(other, int):
            self.number_of_floor += other
            return self

    def __iadd__(self, other):
        if isinstance(other, House):
            self.number_of_floor += other.number_of_floor
            return self
        elif isinstance(other, int):
            self.number_of_floor += other
            return self

    def __radd__(self, other):
        if isinstance(other, House):
            self.number_of_floor = other.number_of_floor + self.number_of_floor
            return self
        elif isinstance(other, int):
            self.number_of_floor = other + self.number_of_floor
            return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) #eq


h1=h1+10
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) #grather than (h1, h2)
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

print(h1 != 15.2) # __ne__

h3=h1
h4=h2

print (h4+h3)
print (h3+h4)

print (h4+15.2) # так как второй аргумент н Int, то будет ошибка (None)
