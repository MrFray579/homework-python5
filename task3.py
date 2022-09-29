def input_position():
    row = int(input('Введите номер строки(от 1 до 3): '))
    while row < 1 or row > 3:
        row = int(input('Вы ошиблись.\nВведите номер строки(от 1 до 3): '))

    columns = int(input('Введите номер столбца(от 1 до 3): '))
    while columns < 1 or columns > 3:
        columns = int(input('Вы ошиблись.\nВведите номер столбца(от 1 до 3): '))
    return row, columns

def check(dask):
    if dask[0][0] == dask[1][0] == dask[2][0] != '*':
        return f'Выиграл {dask[0][0]}'
    elif dask[0][1] == dask[1][1] == dask[2][1] != '*':
        return f'Выиграл {dask[0][1]}'
    elif dask[0][2] == dask[1][2] == dask[2][2] != '*':
        return f'Выиграл {dask[0][2]}'
    elif dask[0][0] == dask[0][1] == dask[0][2] != '*':
        return f'Выиграл {dask[0][0]}'
    elif dask[1][0] == dask[1][1] == dask[2][1] != '*':
        return f'Выиграл {dask[1][0]}'
    elif dask[2][0] == dask[2][1] == dask[2][2] != '*':
        return f'Выиграл {dask[2][0]}'
    elif dask[0][0] == dask[1][1] == dask[2][2] != '*':
        return f'Выиграл {dask[0][0]}' 
    elif dask[0][2] == dask[1][1] == dask[2][0] != '*':
        return f'Выиграл {dask[2][0]}'
    return None           

dask = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

value = ''
i = 0
flag = True
while i < 9 and flag:
    print('\n'.join(['\t'.join(i) for i in dask]))
    if i % 2 == 0:
        print('Ход крестиков: ')
        value = 'x'
    elif i % 2 != 0:
        print('Ход ноликов: ')
        value = 'o'
    row, columns = input_position()

    if dask[row-1][columns-1] != '*':
        print('Позиция занята')
        row, columns = input_position()

    dask[row-1][columns-1] = value
    result = check(dask)
    if result:
        print(result)
        flag = False

    i += 1


