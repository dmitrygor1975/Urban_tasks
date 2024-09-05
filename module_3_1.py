# Задание Модуль 3_1 "Счетчик вызовов"

calls  = 0

def count_calls(): # считаем кол-во вызовов остальных двух функций
    global calls
    calls+=1
    return calls

def string_info (string):
    global calls
    cortage_1 = ()
    cortage_1 = len(string),string.upper(),string.lower()
    count_calls()
    return cortage_1

def is_contains (string, list_to_search):
    global calls
    is_contains = False
    string = string.lower()
    list_to_search = '-'.join(list_to_search).lower()
    #str_2 = list_to_search_1.lower()
    #print(list_to_search, string)

    if string in list_to_search: # проверка на вхождение подстроки в строку
        is_contains=True

    count_calls()
    return is_contains

#string = input("Введите строку:")
#print(string_info(string))

print(string_info('Capybara'))
print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN','Urbans'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
