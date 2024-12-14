# Цикл для добавления элементов в список.

a = [1, 2, "as", (1, 2), 10]
cycle = True
while cycle:
    answer = input("Хотите ввести новый объект в список? (Y/N): ")
    if answer == "Y":
        a.append(input("Введите новый объект: "))
    else:
        cycle = False

print(a[len(a)-1])
print(type(a[len(a)-1]))
print(a)
