# Отсортировать по индексу массы тела (ind = m/h**2)

# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]

result = []

for m, h in data:
    ind = m/(h**2)
    result.append(ind)

result.sort()
print(result)

# Второй вариант решения

print(sorted(data, key = lambda x: x[0] / x[1]**2))

# Найти минимальные элемент из списка выше

print(min(data, key=lambda x: x[0] / x[1] ** 2))


