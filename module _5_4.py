# Модуль 5.4 Задача "История строительства":

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])  # Добавляем новый объект в историю создания
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floor = number_of_floors


    def __del__(self):
        print(f'{self.name} снесен, но остался в истории')


h1 = House('ЖК Эльбрус', 10)
#print(h1)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
#print(h2)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
#print(h3)
print(House.houses_history)

del h2
del h3

# в конце программы удаляет последний экземпляр  ЖК Эльбурус (происходит очистка памяти)
