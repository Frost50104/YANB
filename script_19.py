# Напишите алгоритм, реализованный с помощью вложенных условных операторов, который проверяет заданные условия:
# является ли число целым
# находится ли в промежутке от 100 до 999 включительно
# делится ли одновременно на 2 и на 3

try:
    a = input('Введите число: ')
    a = int(a)
    if type(a) == int:
        if 100 <= a <= 999:
            if a % 2 == 0 and a % 3 == 0:
                print(f"Все условия для числа {a} выполнены")
            else:
                print(f"Число {a} не делится на 2 и на 3 одновременно")
        else:
            print(f"Число {a} находится вне промежутка 100 - 999")
except ValueError:
    print(f"{a} не является целым числом")

# тот-же алгоритм, но объединив все условия в одну строку, используя логические операторы и операторы сравнения:

try:
    b = input('Введите еще одно число: ')
    b = int(b)
    if (type(b) == int) and (100 <= b <= 999) and (b % 2 == 0) and (b % 3 == 0):
        print(f"Все условия для числа {b} выполнены")
    else:
        print(f"Для числа {b} не выполнено одно или несколько условий")
except ValueError:
    print(f"{a} не является целым числом")

#  тот же алгоритм, но все условия объединены через функцию all([]):

try:
    c = input('Введите еще одно число: ')
    c = int(c)
    if all([type(c) == int,
            100 <= c <= 999,
            c % 2 == 0,
            c % 3 == 0]):
        print(f"Все условия для числа {c} выполнены")
    else:
        print(f"Для числа {c} не выполнено одно или несколько условий")
except ValueError:
    print(f"{c} не является целым числом")
