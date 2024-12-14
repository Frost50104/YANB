# Напишите функцию, которая будет возвращать количество делителей числа а.

n = 5

def dividers(n):
    dividers_count = 0
    for i in range(1, n+1):
        if n % i == 0:
            dividers_count += 1
        else:
            continue
    return dividers_count

print(f'У числа {n} есть {dividers(n)} делителя(ей)')