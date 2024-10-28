# Домашнее задание модуль 8.3
# Задача "Некорректность".

class Car:

    def __init__(self, model, vin, number):
        self.model = model

        self.__vin_number = vin #уровень доступа private
        self.car_numbers = number

        Car.__is_valid_vin(self, self.__vin_number)
        Car.__is_valid_numbers(self.car_numbers)

        print (f'{self.model} успешно создан')
        print(f'{self.model} VIN:{self.__vin_number} Number:{self.car_numbers} успешно создан')



    def __is_valid_vin (self, vin_number):

        if not isinstance (vin_number,int):
            raise IncorrectVinNumber('Некорректный тип vin номер',vin_number)

        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber ('Неверный диапазон для vin номер',vin_number)

        else:
            return True

    def __is_valid_numbers (numbers):

        if not isinstance(numbers,str):
            raise IncorrectCarNumber ('Некорректный тип данных для номеров', numbers)

        if len(numbers) != 6:
            raise IncorrectCarNumber ('Неверная длина номера', numbers)

        else:
            return True

class IncorrectVinNumber (Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info
        #print('мы в исключении по VinNumber')
        pass

class IncorrectCarNumber (Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info
        #print('мы в исключении по CarNumber')
        pass

try:
    car1 = Car('Model1', 2000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(f'Ошибка:{exc.message}, смотри -> {exc.info}')
except IncorrectCarNumber as exc:
    print(f'Ошибка:{exc.message}, смотри -> {exc.info}')


try:
    car2 = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(f'Ошибка:{exc.message}, смотри -> {exc.info}')
except IncorrectCarNumber as exc:
    print(f'Ошибка:{exc.message}, смотри -> {exc.info}')

try:
    car3 = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(f'Ошибка:{exc.message}, смотри -> {exc.info}')
except IncorrectCarNumber as exc:
    print(f'Ошибка:{exc.message}, смотри -> {exc.info}')