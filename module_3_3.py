 # Модуль 3.3 Распаковка позиционных параметров

def print_params (a = 1, b = 'строка', c = True):
    print (f"a={a} \n"
           f"b={b} \n"
           f"c={c} \n")

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [100, 'String', False]
values_dict = {'a':111, 'b':222, 'c':333}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка-3' ]
print_params(*values_list_2,  44)
