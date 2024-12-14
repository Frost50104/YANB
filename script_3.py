# Цикл, который ищет наибольший элемент в матрице.
# Цикл, который определяет максимум и минимум каждой строки, а также их индексы.
# Проверка, является ли матрица квадратной (то есть количество строк равно количеству столбцов).

test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]

min_value = []
min_index = []
max_value = []
max_index = []

for row in test_matrix:
    local_min_index = 0
    local_min_value = row[local_min_index]
    local_max_index = 0
    local_max_value = row[local_max_index]
    for element in range(len(row)):
        if row[element] < local_min_value:
            local_min_value = row[element]
            local_min_index = element
        if row[element] > local_max_value:
            local_max_value = row[element]
            local_max_index = element
    min_value.append(local_min_value)
    max_value.append(local_max_value)
    min_index.append(local_min_index)
    max_index.append(local_max_index)

max_element = test_matrix[0][0]
min_element = test_matrix[0][0]

for element in min_value:
    min_element = min_value[0]
    if element < min_element:
        min_element = element

for element in max_value:
    max_element = max_value[0]
    if element > max_element:
        max_element = element

print('\n')
print(f'Наибольший элемент матрицы: {max_element}')
print(f'Наименьший элемент матрицы: {min_element}', '\n')

print(f'Наименьшие элементы матрицы: {min_value}')
print(f'Индексы наименьших элементов матрицы: {min_index}')
print(f'Наибольшие элементы матрицы: {max_value}')
print(f'Индексы наибольших элементов матрицы: {max_index}', '\n')

print('Матрица квадратная?')
print(True) if len(test_matrix) == len(test_matrix[0]) else print(False)
