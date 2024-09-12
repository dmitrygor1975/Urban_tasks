# Модуль 3.5 Задача "Рекурсивное умножение цифр"

def get_multiplied_digits (number:int):

    str_number = str (number)
    first = int(str_number[0])

    if len(str_number)>1:
        result = first*get_multiplied_digits(int(str_number[1:]))
    else: result = first

    return result

result1 = get_multiplied_digits(123)
result2 = get_multiplied_digits(222)
result3 = get_multiplied_digits(40203)

print (result1)
print (result2)
print (result3)
