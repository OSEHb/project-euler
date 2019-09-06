'''Задача 51'''
# Меняя первую цифру числа *3 (двузначного числа, заканчивающегося цифрой 3), оказывается, что шесть из девяти
# возможных значений - 13, 23, 43, 53, 73 и 83 - являются простыми числами.
# При замене третьей и четвертой цифры числа 56**3 одинаковыми цифрами, получаются десять чисел,
# из которых семь - простые: 56003, 56113, 56333, 56443, 56663, 56773 и 56993. Число 56**3 является наименьшим числом,
# подставление цифр в которое дает именно семь простых чисел. Соответственно, число 56003, будучи первым из полученных
# простых чисел, является наименьшим простым числом, обладающим указанным свойством.
# Найдите наименьшее простое число, которое является одним из восьми простых чисел, полученных заменой части цифр
# (не обязательно соседних) одинаковыми цифрами.

from math import sqrt, floor

table = {}  # Время работы 38сек


def result_func(arg):  # Сравниваю оставшиеся два числа в полученых числах
    a = 0
    b = 0

    for n in arg:
        if n == 'f1':
            a = 3
            b = 4
        if n == 'f2':
            a = 0
            b = 1
        if n == 'f3':
            a = 1
            b = 3
        if n == 'f4':
            a = 0
            b = 4

        for i in table[n]:
            result = []
            index = 0
            i = str(i)
            del table[n][0]
            for j in table[n]:
                j = str(j)
                if j[a] == i[a] and j[b] == i[b]:
                    result.append(int(j))
                    index += 1
                if index == 8:
                    print(result)
                    return print('result:', result[0])


# Делю числа по расположению одинаковых цифр. Если их 3(что я выделил в sot_prime()),
# то всего 4 варианта их расположения f1, f2, f3, f4
def filter(arg):
    table['f1'] = []
    table['f2'] = []
    table['f3'] = []
    table['f4'] = []

    for i in arg:
        i = str(i)
        if i[0] == i[1] == i[2]:
            table['f1'].append(int(i))
        if i[2] == i[3] == i[4]:
            table['f2'].append(int(i))
        if i[0] == i[2] == i[4]:
            table['f3'].append(int(i))
        if i[1] == i[2] == i[3]:
            table['f4'].append(int(i))

    result_func(table)


def sot_prime(arg):  # Как минимум 3 числа в цифре должны повторятся кроме последнего (ну, я так решил)))
    noms = []

    for i in arg:
        i = str(i)
        for k in range(10):
            index = 0
            for j in i[:5]:
                if int(j) == k:
                    index += 1
                if index >= 3:
                    noms.append(int(i))
                    break

    filter(noms)


def prime3():  # Нахожу простые числа закончив-ся на 3
    nums = []

    for i in range(100001, 1000000, 2):
        for j in range(1, i + 1, 2):
            if j > int(floor(sqrt(i) + 1)):
                if str(i)[-1] == '3':
                    nums.append(i)
                    break
                else:
                    break
            elif i % j == 0 and j != 1:
                break

    sot_prime(nums)


prime3()
