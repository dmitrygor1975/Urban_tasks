# Модуль 5.2 Задача "Магические здания":

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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#h1.__str__()
#h2.__str__()

print(h1)
print(h2)

print(len(h1))
print(len(h2))
