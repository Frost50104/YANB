field = [['0', '', 'X'],
        ['0', 'X', ' '],
        ['X', ' ', '0']]

# Проверка по строкам поля
for i in range(3):
    row = []
    for j in range(3):
        row.append(field[i][j])
    if row == ['X', 'X', 'X']:
        print('Выйграл X!')
    elif row == ['0', '0', '0']:
        print('Выйграл 0!')

    # Проверка по столбцам поля
for i in range(3):
    row = []
    for j in range(3):
        row.append(field[j][i])
    if row == ['X', 'X', 'X']:
        print('Выйграл X!')
    elif row == ['0', '0', '0']:
        print('Выйграл 0!')

    # Проверка по диагонали
if field[0][0] == field[1][1] == field[2][2] == 'X':
    print('Выйграл X!')
elif field[0][2] == field[1][1] == field[2][0] == 'X':
    print('Выйграл X!')
if field[0][0] == field[1][1] == field[2][2] == '0':
    print('Выйграл 0!')
elif field[0][2] == field[1][1] == field[2][0] == '0':
    print('Выйграл 0!')

