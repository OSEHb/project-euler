'''Задача 47'''
# Первые два последовательные числа, каждое из которых имеет два отличных друг от друга простых множителя:
# 14 = 2 × 7
# 15 = 3 × 5
# Первые три последовательные числа, каждое из которых имеет три отличных друг от друга простых множителя:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Найдите первые четыре последовательных числа, каждое из которых имеет четыре отличных друг от друга простых множителя.
# Каким будет первое число?

from math import sqrt, floor
from sys import maxsize

result = []
numbers = []


def prime(arg1, arg2, arg3, arg4):
    nums = [arg1, arg2, arg3, arg4]

    for i in nums:
        if i == 2:
            continue
        elif i % 2 == 0 and sqrt(i).is_integer() == False:
            return

        for j in range(1, i + 1, 2):
            if j > int(floor(sqrt(i) + 1)):
                break
            elif i % j == 0 and j != 1:
                if sqrt(i).is_integer() == True:
                    xx = int(sqrt(i))
                    for x in range(1, xx, 2):
                        if x > int(floor(sqrt(xx) + 1)):
                            break
                        elif xx % x == 0 and x != 1:
                            return
                else:
                    return

    return arg1, arg2, arg3, arg4


def div(arg):
    proven = []
    lst = []

    for i in range(2, arg):
        if len(lst) > 0 and None not in lst:
            break

        elif arg % i == 0:
            _arg = arg // i

            for j in range(i + 1, _arg):
                if len(lst) > 0 and None not in lst:
                    break
                elif _arg % j == 0:
                    _arg_ = _arg // j

                    for x in range(j + 1, _arg_):
                        if len(lst) > 0 and None not in lst:
                            break
                        elif _arg_ % x == 0:
                            lst = []
                            _a_r_g_ = _arg_ // x

                            if _a_r_g_ * x * j * i == arg:
                                if i in proven:
                                    break
                                else:
                                    proven.extend([i, j, x, _a_r_g_])
                                    lst.append(prime(i, j, x, _a_r_g_))

    if len(lst) == 0:
        return None
    else:
        return lst[0]


'''Спустя ЧАСЫ! ожидания, получив верный ответ, установил начало цикла на 130000(по ближе к ответу). 
Программа работает ОЧЕНЬ медленно!!!'''
for n in range(130000, maxsize ** 10):
    print(n)
    if len(result) == 4 and len(numbers) == 16:
        print(result[0], ':', numbers[0:4], result[1], ':', numbers[4:8], result[2], ':', numbers[8:12], result[3], ':',
              numbers[12:16])
        print('result:', result[0])
        break
    else:
        divs = div(n)

        if divs != None:
            if divs[0] != divs[1] != divs[2] != divs[3] != divs[0] != divs[2] and divs[3] != divs[1]:
                if divs[0] not in numbers:
                    if divs[1] not in numbers:
                        if divs[2] not in numbers:
                            numbers.extend([divs[0], divs[1], divs[2], divs[3]])
                            result.append(n)

        else:
            result = []
            numbers = []
