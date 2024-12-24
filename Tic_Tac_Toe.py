
# Поле
field = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

num = 0
win = None

# Функция отображения поля
def show_field(field=field):
    print("  | 0 | 1 | 2 |")
    for i in range(3):
        print(f'{i} | {' | '.join(field[i])} |')
        print('_______________')


# Ввод пользователя
def ask():
    while True:
        x_and_y = input('Введите координаты: ').split()

        if len(x_and_y) != 2:
            print('Введите два числа!')
            continue

        x, y = x_and_y

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == ' ':
                return x, y
            else:
                print('Клетка занята!')
        else:
            print('Введены неверные координаты!')

# Условие победы
def winner(field=field):
    global win
    # Проверка по строкам поля
    for i in range(3):
        row = []
        for j in range(3):
            row.append(field[i][j])
        if row == ['X', 'X', 'X']:
            print('Выйграл X!')
            win = True
            return win
        elif row == ['0', '0', '0']:
            print('Выйграл 0!')
            win = True
            return win

    # Проверка по столбцам поля
    for i in range(3):
        row = []
        for j in range(3):
            row.append(field[j][i])
        if row == ['X', 'X', 'X']:
            print('Выйграл X!')
            win = True
            return win
        elif row == ['0', '0', '0']:
            print('Выйграл 0!')
            win = True
            return win

    # Проверка по диагонали
    if field[0][0] == field[1][1] == field[2][2] == 'X':
        print('Выйграл X!')
        win = True
        return win
    elif field[0][2] == field[1][1] == field[2][0] == 'X':
        print('Выйграл X!')
        win = True
        return win
    if field[0][0] == field[1][1] == field[2][2] == '0':
        print('Выйграл 0!')
        win = True
        return win
    elif field[0][2] == field[1][1] == field[2][0] == '0':
        print('Выйграл 0!')
        win = True
        return win

# Игра
while True:
    num +=1
    show_field()
    winner()
    if win == True:
        break
    if num == 10:
        print('Ничья')
        break

    print(f'Ход номер {num}')

    if num % 2 == 1:
        print('Ходит X')
    else:
        print('Ходит 0')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

