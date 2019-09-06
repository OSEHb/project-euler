'''Задача 24'''
# Перестановка - это упорядоченная выборка объектов. К примеру, 3124 является одной из возможных перестановок
# из цифр 1, 2, 3 и 4. Если все перестановки приведены в порядке возрастания или алфавитном порядке,
# то такой порядок будем называть словарным. Словарные перестановки из цифр 0, 1 и 2 представлены ниже:
# 012   021   102   120   201   210
# Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?

n = 0
result = []
nom = '0123456789'
for a in nom:
    nom0 = nom.replace(a, '')
    if n == 1000000:
        break
    for b in nom0:
        nom1 = nom0.replace(b, '')
        if n == 1000000:
            break
        for c in nom1:
            nom2 = nom1.replace(c, '')
            if n == 1000000:
                break
            for d in nom2:
                nom3 = nom2.replace(d, '')
                if n == 1000000:
                    break
                for e in nom3:
                    nom4 = nom3.replace(e, '')
                    if n == 1000000:
                        break
                    for f in nom4:
                        nom5 = nom4.replace(f, '')
                        if n == 1000000:
                            break
                        for g in nom5:
                            nom6 = nom5.replace(g, '')
                            if n == 1000000:
                                break
                            for h in nom6:
                                nom7 = nom6.replace(h, '')
                                if n == 1000000:
                                    break
                                for i in nom7:
                                    nom8 = nom7.replace(i, '')
                                    if n == 1000000:
                                        break
                                    for j in nom8:
                                        result = []
                                        result.append(a + b + c + d + e + f + g + h + i + j)
                                        print(result)
                                        n += 1
                                        if n == 1000000:
                                            break

print('result:', result)
