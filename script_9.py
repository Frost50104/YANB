# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.

def multiplication(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiplication(1, 2, ))