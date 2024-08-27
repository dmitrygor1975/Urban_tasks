#версия - 2 (с одним циклом For)

def get_matrix(n, m, value):
   matrix = []

   for i in range(n):           # количество строк матрицы = n
       matrix.append([])        # добавляем пустой элемент строки
       matrix[i] = [value] * m  # пополняем пустой список значением [Value]
                                # и умножаем список на количество столбцов матрицы = m
   return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)