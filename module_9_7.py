# Декораторы
def is_prime(func):
    def wrapper(*args):
        number = func(*args) # результат суммы треъ чисел
        for i in range(2, number): # не делаем проверку суммы чисел на ноль или единицу
            if number % i == 0:
                return (f'составное число \n{number}') #False
        return (f'простое число \n{number}') #True
    return wrapper


"""def is_prime(func):
    def wrapper(x,y,z):
        number = func(x, y, z)
        for i in range(2, number//2+1): # проверка целочисл// деления от 2 до половины проверяемого числа
            if number % i == 0:
                return (f'составное число \n{number}') #False
        return (f'простое число \n{number}') #True
    return wrapper"""

@ is_prime

def sum_three(x, y, z):
    res=x+y+z
    return res

print (sum_three(2, 3, 6))




