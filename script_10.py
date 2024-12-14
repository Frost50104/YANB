# С помощью рекурсивной функции найдите сумму чисел от 1 до n

n = 5

def sum_cycle(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sum_cycle(n))

def sum_rec(n):
    if n == 1:
        return 1
    return n + sum_rec(n-1)

print(sum_rec(n))

# С помощью рекурсивной функции развернуть строку

text = '12345'
print(text[::-1])

def reverse_str(text):
   if len(text) == 0:
       return ''
   else:
       return text[-1] + reverse_str(text[:-1])

print(reverse_str(text))

# Дано натуральное число N. Вычислите сумму его цифр

N = 125

def sum_of_N_cycle(N):
    sum = 1
    while N > 1:
        sum += N % 10
        N = N // 10
    return sum

print(sum_of_N_cycle(N))

def sum_of_N(N):
    if N < 10:
        return N
    return N % 10 + sum_of_N(N // 10)

print(sum_of_N(N))