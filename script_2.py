# Алгоритм подбора варианта одежды в зависимости от условий.

temperature = int(input('Введите температуру: '))
is_rainy = False
is_raining_heavily = False

if 20 < temperature < 30:
    is_rainy = input('Идет ли дождь: ') == 'да'
    if is_rainy:
        print('Футболку, шорты и дождевик')
    else:
        print('Футболку и шорты')
else:
    if temperature > 0:
        is_rainy = input('Идет ли дождь: ') == 'да'
        if is_rainy:
            is_raining_heavily = input('Дождь сильный: ') == 'да'
            if is_raining_heavily:
                print('Пальто, резиновые сапоги и зонт')
            else:
                print('Пальто и дождевик')
        else:
            print('Пальто')
    else:
        print('Пуховик')

