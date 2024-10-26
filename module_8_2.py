# Домашнее задание к модулю 8_2 "Задача "План перехват":"

def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    numb = list(*numbers)
    numbers = numb
    #pr_1 = isinstance(numbers,(list, float,int))
    #pr_2 = isinstance(numbers, (str))

    for i in numbers:
        try:
            result += i

        except TypeError:
            print(f'В numbers записан некорректный тип данных для подсчета суммы - {i}')
            incorrect_data += 1

    return (result, incorrect_data)

def calculate_average(*numbers):
    try:
        sum = personal_sum(*numbers)
        count_of_numbers = len(*numbers)-sum[1]
        result_2 = sum[0] /count_of_numbers
        return result_2

    except ZeroDivisionError:
       return (0)

    except TypeError:
        print(f'В numbers записан некорректный тип данных')

#print(personal_sum((1,'b',3)))
#print(personal_sum([42, 15, 36, 13]))

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
