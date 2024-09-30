# Домашнее задание по уроку "Пространство имен"

def test_function ():

    def inner_function ():
        print("Я в области видимости функции test_function")
        return
    inner_function()

    return

test_function()

#inner_function() # вывод ошибки в консоль - NameError: name 'inner_function' is not defined.