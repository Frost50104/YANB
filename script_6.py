# Функция для определения является ли число n делителем числа a
# Функция для печати лесенки

def divider(a, n):
    if a%n == 0:
        print(f'Число {n} является делителем числа {a}')
    else:
        print(f'Число {n} не является делителем числа {a}')

divider(6, 2)
divider(5, 2)

print()

def stairs(n=5):
    for i in range(n, 0, -1):
        print('*' * i)

stairs()
