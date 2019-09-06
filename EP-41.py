'''Задача 41'''
# Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до n используется в нем ровно один раз.
# К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.
# Какое существует наибольшее n-значное пан-цифровое простое число?

from math import sqrt

result_nom = []

def func3():
    nom = '7654321'

    for a in nom:
        nom0 = nom.replace(a, '')
        for b in nom0:
            nom1 = nom0.replace(b, '')
            for c in nom1:
                nom2 = nom1.replace(c, '')
                for d in nom2:
                    nom3 = nom2.replace(d, '')
                    for e in nom3:
                        nom4 = nom3.replace(e, '')
                        for f in nom4:
                            nom5 = nom4.replace(f, '')
                            for g in nom5:
                                result = a + b + c + d + e + f + g
                                result = int(result)

                                if result % 2 == 0:
                                    break

                                else:
                                    for div in range(3, result, 2):
                                        if div > int(sqrt(result) + 1):
                                            return result_nom.append(result)

                                        elif result % div == 0:
                                            break


def func2():
    nom = '87654321'

    for a in nom:
        nom0 = nom.replace(a, '')
        for b in nom0:
            nom1 = nom0.replace(b, '')
            for c in nom1:
                nom2 = nom1.replace(c, '')
                for d in nom2:
                    nom3 = nom2.replace(d, '')
                    for e in nom3:
                        nom4 = nom3.replace(e, '')
                        for f in nom4:
                            nom5 = nom4.replace(f, '')
                            for g in nom5:
                                nom6 = nom5.replace(g, '')
                                for h in nom6:
                                    result = a + b + c + d + e + f + g + h
                                    result = int(result)

                                    if result % 2 == 0:
                                        break

                                    else:
                                        for div in range(3, result, 2):
                                            if div > int(sqrt(result) + 1):
                                                return result_nom.append(result)

                                            elif result % div == 0:
                                                break

    func3()


def func():
    nom = '987654321'

    for a in nom:
        nom0 = nom.replace(a, '')
        for b in nom0:
            nom1 = nom0.replace(b, '')
            for c in nom1:
                nom2 = nom1.replace(c, '')
                for d in nom2:
                    nom3 = nom2.replace(d, '')
                    for e in nom3:
                        nom4 = nom3.replace(e, '')
                        for f in nom4:
                            nom5 = nom4.replace(f, '')
                            for g in nom5:
                                nom6 = nom5.replace(g, '')
                                for h in nom6:
                                    nom7 = nom6.replace(h, '')
                                    for i in nom7:
                                        result = a + b + c + d + e + f + g + h + i
                                        result = int(result)

                                        if result % 2 == 0:
                                            break

                                        else:
                                            for div in range(3, result, 2):
                                                if div > int(sqrt(result) + 1):
                                                    return result_nom.append(result)

                                                elif result % div == 0:
                                                    break

    func2()


func()

print('result:', result_nom)

