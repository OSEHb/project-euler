'''Задача 35.'''
# Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми
# числами: 197, 719 и 971.
# Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
# Сколько существует круговых простых чисел меньше миллиона?

from math import sqrt
from time import process_time

result = [2, ]


def nom(arg):
    strarg = str(arg)
    rev = []

    if len(strarg) == 2:
        while True:
            revarg = strarg[-1] + strarg[0]

            if int(revarg) == arg:
                if rev == []:
                    return result.append(arg)

                else:
                    rev.append(arg)
                    for s in rev:
                        result.append(s)
                    return None

            else:
                if int(revarg) % 2 == 0:
                    return None

                for n in range(3, int(revarg) + 1, 2):
                    if n > int((sqrt(int(revarg))) + 1):
                        strarg = revarg
                        rev.append(int(revarg))
                        break

                    elif int(revarg) % n == 0:
                        return None

    elif len(strarg) == 3:
        while True:
            revarg = strarg[-1] + strarg[0] + strarg[1]

            if int(revarg) == arg:
                if rev == []:
                    return result.append(arg)

                else:
                    rev.append(arg)
                    for s in rev:
                        result.append(s)
                    return None

            else:
                if int(revarg) % 2 == 0:
                    return None

                for n in range(3, int(revarg) + 1, 2):
                    if n > int((sqrt(int(revarg))) + 1):
                        strarg = revarg
                        rev.append(int(revarg))
                        break

                    elif int(revarg) % n == 0:
                        return None

    elif len(strarg) == 4:
        while True:
            revarg = strarg[-1] + strarg[0] + strarg[1] + strarg[2]

            if int(revarg) == arg:
                if rev == []:
                    return result.append(arg)

                else:
                    rev.append(arg)
                    for s in rev:
                        result.append(s)
                    return None

            else:
                if int(revarg) % 2 == 0:
                    return None

                for n in range(3, int(revarg) + 1, 2):
                    if n > int((sqrt(int(revarg))) + 1):
                        strarg = revarg
                        rev.append(int(revarg))
                        break

                    elif int(revarg) % n == 0:
                        return None

    elif len(strarg) == 5:
        while True:
            revarg = strarg[-1] + strarg[0] + strarg[1] + strarg[2] + strarg[3]

            if int(revarg) == arg:
                if rev == []:
                    return result.append(arg)

                else:
                    rev.append(arg)
                    for s in rev:
                        result.append(s)
                    return None

            else:
                if int(revarg) % 2 == 0:
                    return None

                for n in range(3, int(revarg) + 1, 2):
                    if n > int((sqrt(int(revarg))) + 1):
                        strarg = revarg
                        rev.append(int(revarg))
                        break

                    elif int(revarg) % n == 0:
                        return None

    elif len(strarg) == 6:
        while True:
            revarg = strarg[-1] + strarg[0] + strarg[1] + strarg[2] + strarg[3] + strarg[4]

            if int(revarg) == arg:
                if rev == []:
                    return result.append(arg)

                else:
                    rev.append(arg)
                    for s in rev:
                        result.append(s)
                    return None

            else:
                if int(revarg) % 2 == 0:
                    return None

                for n in range(3, int(revarg) + 1, 2):
                    if n > int((sqrt(int(revarg))) + 1):
                        strarg = revarg
                        rev.append(int(revarg))
                        break

                    elif int(revarg) % n == 0:
                        return None


for i in range(3, 1000000, 2):
    if i in result:
        continue

    for j in range(1, i + 1, 2):
        if j > int((sqrt(i)) + 1):
            if len(str(i)) == 1:
                result.append(i)
                break

            elif len(str(i)) > 1 and i not in result:
                nom(i)
                break

        elif i % j == 0 and j != 1:
            break

print('result:', len(result), 'Time:', process_time(), 's')
