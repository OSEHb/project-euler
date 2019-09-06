'''Задача 49'''
# Арифметическая прогрессия: 1487, 4817, 8147, в которой каждый член возрастает на 3330, необычна в двух отношениях:
# (1) каждый из трех членов является простым числом, (2) все три четырехзначные числа являются перестановками друг друга.
# Не существует арифметических прогрессий из трех однозначных, двухзначных и трехзначных простых чисел,
# демонстрирующих это свойство. Однако, существует еще одна четырехзначная возрастающая арифметическая прогрессия.
# Какое 12-значное число образуется, если объединить три члена этой прогрессии?

from math import sqrt, floor


def result_lst(arg):
    ln = len(arg)
    tabl = {}
    index = 0
    for x in arg:
        index += 1
        if index == ln:
            break

        for y in (arg[index:]):
            yx = int(y) - int(x)
            if yx == 3330:
                if yx not in tabl:
                    tabl[yx] = (y, x)
                else:
                    if x in tabl[yx]:
                        print(tabl[yx][1] + x + y)
                        return None
    return None


def lst_nums(arg):
    index = 0
    for x in arg:
        x = str(x)
        n1 = x[0]
        n2 = x[1]
        n3 = x[2]
        n4 = x[3]
        index += 1
        lst_result = []
        if arg[index] == arg[-1]:
            break

        for y in arg[index:]:
            y = str(y)
            if n1 in y and n2 in y:
                if n3 in y and n4 in y:
                    lst_result.extend([x, y])
            else:
                continue

        if len(set(lst_result)) >= 3:
            result_lst(sorted(set(lst_result)))

    return None


def div(arg):
    if arg % 2 == 0:
        return
    for x in range(1, arg):
        if x > int(floor(sqrt(arg) + 1)):
            return arg
        elif arg % x == 0 and x != 1:
            return


def nums(a, b):
    lst = []
    for i in range(a, b):
        str_i = str(i)
        if str_i[0] != str_i[1] != str_i[2]:
            if div(i) != None:
                lst.append(i)
    return lst_nums(lst)

nums(1000, 10000)
