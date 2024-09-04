from http.cookiejar import uppercase_escaped_char
from idlelib.debugobj_r import remote_object_tree_item

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

#def is_contains (string, list_to_search):

string = input("Введите строку:")
print(string_info(string))

print(string_info('Capybara'))

#print(string_info('Armageddon'))
#print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
#print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
