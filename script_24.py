# Создать класс прямоугольник
# где в конструкторе задаются атрибуты: начальные координаты x, y, width и height
# метод должен вернуть строку Rectangle : 5, 10, 50, 100.

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_info(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'

    def square(self):
        return f'Square: {self.width * self.height}'

rectangle_1 = Rectangle(x=5, y=10, width=50, height=100)

print(rectangle_1.get_info())
print(rectangle_1.square())

# Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.
# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»

# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def get_all_info(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'

    def get_info(self):
        return self.name, self.surname, self.city

client_1 = Client(name='Иван', surname='Петров', city='Москва', balance='50')
print(client_1.get_all_info())

client_2 = Client(name='Петр', surname='Иванов', city='Красноярск', balance='1000')

clients = [client_1, client_2]

for client in clients:
    print(client.get_info())