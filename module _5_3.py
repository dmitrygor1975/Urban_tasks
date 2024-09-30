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
        return self.number_of_floor == other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        self.number_of_floor += value
        return self

    def __iadd__(self, value):
        self.number_of_floor += value
        return self

    def __radd__(self, value):
        self.number_of_floor = value + self.number_of_floor
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
