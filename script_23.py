from test_zone import Rectangle
from test_zone import Cat

r1 = Rectangle(width=20, height=11)

print("r1.width =", r1.width)
print("r1.height =", r1.height)
print("r1.get_width =", r1.get_width())
print("r1.get_height =", r1.get_height())
print("r1.get_area =", r1.get_area())

cat_1 = Cat(name='Sam', gender='male', age=2)

print('Имя:', cat_1.get_name())
print('Пол:', cat_1.get_gender())
print('Возраст:', cat_1.get_age())

# Создайте класс Dog с помощью наследования класса Cat.
# Создайте метод get_pet() таким образом, чтобы он возвращал только имя и возраст.

class Dog(Cat):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.gender = gender
        self.age = age

    def get_pet(self):
        return f'{self.name} {self.age}'

dog_1 = Dog("Felix", "boy", 2)
print(dog_1.get_pet())