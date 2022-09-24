from random import randint as rd
from sys import exit

def check_win(m, n):
    if m == 1 and n == 0:
        return 'Выиграл бот'
    elif m == 0 and n == 0:
        return 'Вы выиграли!'
    return None


j = 0
n = 2021
while n > 0:
    if n >= 28:
        count_user = int(input('Сколько Вы хотите взять конфет? (от 1 до 28): '))
        while count_user < 1 or count_user > 28:
            count_user = int(input('Вы ошиблись. Попробуйте снова.\nСколько Вы хотите взять конфет? (от 1 до 28): '))
    else:
        count_user = int(input(f'Сколько Вы хотите взять конфет? (от 1 до {n}): '))
        while count_user < 1 or count_user > n:
            count_user = int(input(f'Вы ошиблись. Попробуйте снова.\nСколько Вы хотите взять конфет? (от 1 до {n}): '))

    n -= count_user
    print(f'Вы взяли {count_user} конфет.\nОсталось {n} конфет.')
    result = check_win(j, n)
    if result:
        print(result)
        exit()
    j = 1
    if n < 28:
        count_bot = rd(1, n)
    else:
        count_bot = rd(1, 29)
    n -= count_bot
    print(f'Бот взял {count_bot} конфет.\nОсталось {n} конфет.')
    result = check_win(j, n)
    if result:
        print(result)
        exit()
