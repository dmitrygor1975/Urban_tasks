numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Rnumbers = [5, 2, 4, 3, 11, 15, 2]
primes = [] #простые числа
not_primes = [] #составные числа

## is_true = True ЛИШНЯЯ СТРОКА

for i in range(len(numbers)):
    is_true = True # всегда в начале цикла перебора устанавливаем флаг = True
    if numbers[i] == 1: #проверка если число = 1, то переходим на новый цикл i
        continue # если число = 1, то переход на новый цикл
    else:
        for k in range(2,numbers[i]):   # диапазон делителей от 2 до заданного числа;
                                        # для числа 2 цикл не будет выполняться ->
                                        # сразу переходим на фиксацию 2 как простое число
            #is_true = True
            if numbers[i] % k == 0:
                is_true = False
                break #если остаток нуль, то переход на новое число в списке и фиксируем составное число
    if is_true:
        primes.extend([numbers[i]])
    elif not is_true:
        not_primes.extend([numbers[i]])

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')