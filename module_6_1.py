# задача Съедобное, несъедобное

class Animal:
    alive = True    # живой
    fed = False     # накормленный

    def __init__(self, name):
        self.name = name

class Plant:
    edible = False # съедобность

    def __init__(self, name):
        self.name = name

class Mammal (Animal):

    def eat (self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True

        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator (Animal):

    def eat (self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Flower (Plant):
    #def __init__(self, name):
    #    self.name = name
    pass

class Fruit (Plant):
    #def __init__(self, name):
    #    self.name = name
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

p3 = Flower('Ромашка')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)