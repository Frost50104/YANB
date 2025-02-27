# функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
# По умолчанию, она начинается с единицы и шагом 1, но пользователь может указать
# любой шаг и любое число в качестве аргумента функции,
# с которого будет начинаться последовательность.

def generator(start, step):
    counter = start
    while True:
        yield counter
        counter += step

sequence = generator(start=1, step=1) # упаковываем ее в переменную

for i in range(10): # выводим первые 10 числ из генератора
    print(next(sequence))