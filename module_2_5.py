# версия - 1 (два цикла For)

def get_matrix(n, m, value):
    matrix = []

    for i in range(n):          # количество строк матрицы = n
        matrix.append([1]*m)    # добавляем строку и записываем любое непустое значение  = количеству столбцов m
        #matrix.append([])      # либо вариант стр 8 + стр 9
        #matrix [i] = [2]*m     #
        for k in range(m):          # количество столбцов матрицы = m
            matrix [i][k] = value   # записываем в каждый столбец значение =value
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)