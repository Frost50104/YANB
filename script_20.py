# Напишите программу, которая на вход принимает последовательность целых чисел, и возвращает True,
# если все числа ненулевые, и False, если хотя бы одно число равно 0

a = "10 12 1"
a = a.split()
a = list(map(int, a))
result = None
for i in a:
    if i != 0:
        result = True
    else:
        result = False
        break


print(f'1. Все элементы являются ненулевыми: {result}')

# альтернативный способ решения

L = "10 12 1"
L = list(map(int, L.split()))

print(f'2. Все элементы являются ненулевыми: {all(L)}')

# Напишите программу, которая на вход принимает последовательность целых чисел и возвращает True,
# если все числа равны нулю, и False, если найдется хотя бы одно ненулевое число.
# Разрешается использование только логических операторов и функций all([ ]) и any([ ]).

b = "0 0 0"
b = list(map(int, b.split()))

print(f'3. Все элементы являются нулевыми: {not any(b)}')