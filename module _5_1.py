# Модуль 5.1 Атрибуты и методы объекта

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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

#print(h1.name,h1.number_of_floor)
h1.go_to(10)
h2.go_to(5)
