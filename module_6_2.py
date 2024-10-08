# задача Изменять нельзя получать


class Vehicle:
    __COLOR_VARIANTS = ['red','blue','green','black', 'white']

    def __init__(self, owner, __model, __color, __engine_power ):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model (self):
        print (f'модель {self.__model}')

    def get_horse_power (self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color (self):
        print(f'Цвет:{self.__color}')
    
    def print_info (self):
        self.get_model()
        self.get_horse_power()
        self.get_color()
        print(f'Владелец: {self.owner}')


    def set_color (self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"нельзя поменять цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan ('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
#vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')

#vehicle1.get_model()
#vehicle1.get_horse_power()
#vehicle1.get_color()

vehicle1.owner = 'Vasyok'

# Проверяем что поменялось

vehicle1.print_info()
