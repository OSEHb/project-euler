'''Задача 43'''
# Число 1406357289, является пан-цифровым, поскольку оно состоит из цифр от 0 до 9 в определенном порядке.
# Помимо этого, оно также обладает интересным свойством делимости подстрок.
# Пусть d1 будет 1-ой цифрой, d2 будет 2-ой цифрой, и т.д. В таком случае, можно заметить следующее:
# d2d3d4=406 делится на 2 без остатка
# d3d4d5=063 делится на 3 без остатка
# d4d5d6=635 делится на 5 без остатка
# d5d6d7=357 делится на 7 без остатка
# d6d7d8=572 делится на 11 без остатка
# d7d8d9=728 делится на 13 без остатка
# d8d9d10=289 делится на 17 без остатка
# Найдите сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих данным свойством.

result = 0  # Время работы 50сек
noms = '0123456789'
table = {}
key = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10']

for a in noms:
    nom0 = noms.replace(a, '')
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
                                    nom8 = nom7.replace(i, '')
                                    for j in nom8:
                                        result_nom = a + b + c + d + e + f + g + h + i + j
                                        nom = result_nom

                                        for d_key in key:
                                            for d_nom in nom:
                                                table[d_key] = d_nom
                                                nom = nom.replace(nom[0], '')
                                                break

                                        if int(table['d2'] + table['d3'] + table['d4']) % 2 == 0:
                                            if int(table['d3'] + table['d4'] + table['d5']) % 3 == 0:
                                                if int(table['d4'] + table['d5'] + table['d6']) % 5 == 0:
                                                    if int(table['d5'] + table['d6'] + table['d7']) % 7 == 0:
                                                        if int(table['d6'] + table['d7'] + table['d8']) % 11 == 0:
                                                            if int(table['d7'] + table['d8'] + table['d9']) % 13 == 0:
                                                                if int(
                                                                        table['d8'] + table['d9'] + table[
                                                                            'd10']) % 17 == 0:
                                                                    result += int(result_nom)
                                                                else:
                                                                    break
                                                            else:
                                                                break
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                else:
                                                    break
                                            else:
                                                break
                                        else:
                                            break

print(result)

