# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной содержащей, количество вызовов, используйте nonlocal область декоратора.

def my_decorator(fn):
    count = 0
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        nonlocal count
        count += 1
        print(f'Функция {fn} была выполнена {count} раз')
        return result, count
    return wrapper

@my_decorator
def test_func():
    print('Hello!')

for i in range(0, 10):
    test_func()
