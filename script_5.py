# Алгоритм, который определяет, содержит ли число запрашиваемую цифру, не приводя число в строку.

number = 1235678910

digit_to_find = int(input('Введите число: '))

num = number
while num > 1:
    element = num % 10
    if element == digit_to_find:
        print(f'Цифра {digit_to_find} содержится в числе {number}')
        break
    num = num // 10
