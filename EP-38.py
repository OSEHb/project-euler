'''Задача 38.'''
# Возьмем число 192 и умножим его по очереди на 1, 2 и 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# Объединяя все три произведения, получим девятизначное число 192384576 из цифр от 1 до 9 (пан-цифровое число).
# Будем называть число 192384576 объединенным произведением 192 и (1,2,3)
# Таким же образом можно начать с числа 9 и по очереди умножать его на 1, 2, 3, 4 и 5, что в итоге дает пан-цифровое
# число 918273645, являющееся объединенным произведением 9 и (1,2,3,4,5).
# Какое самое большое девятизначное пан-цифровое число можно образовать как объединенное произведение целого числа и
# (1,2, ... , n), где n > 1?

result = 0
nom = ''
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 1
n1 = []
n2 = []
n3 = []
n4 = []
n5 = []
n6 = []
n7 = []
n8 = []
n9 = []

while len(n) > 1:
    for j in n:
        pan = str(i * j)
        nom = nom + pan

    if len(nom) > 9:
        n.pop()
        i = 1
        nom = ''

    elif len(nom) == 9:
        for int_nom in nom:
            if int_nom == '0':
                nom = '0'
                n1, n2, n3, n4, n5, n6, n7, n8, n9 = [], [], [], [], [], [], [], [], []
                break

            if int_nom == '1':
                n1.append(int(int_nom))
                continue

            elif int_nom == '2':
                n2.append(int(int_nom))
                continue

            elif int_nom == '3':
                n3.append(int(int_nom))
                continue

            elif int_nom == '4':
                n4.append(int(int_nom))
                continue

            elif int_nom == '5':
                n5.append(int(int_nom))
                continue

            elif int_nom == '6':
                n6.append(int(int_nom))
                continue

            elif int_nom == '7':
                n7.append(int(int_nom))
                continue

            elif int_nom == '8':
                n8.append(int(int_nom))
                continue

            elif int_nom == '9':
                n9.append(int(int_nom))

        if len(n1) > 1 or len(n2) > 1 or len(n3) > 1 or len(n4) > 1 or len(n5) > 1 or len(n6) > 1 or len(n7) > 1 \
            or len(n7) > 1 or len(n8) > 1 or len(n9) > 1:
            i += 1
            nom = ''
            n1, n2, n3, n4, n5, n6, n7, n8, n9 = [], [], [], [], [], [], [], [], []

        elif int(nom) > result:
            i += 1
            result = int(nom)
            nom = ''
            n1, n2, n3, n4, n5, n6, n7, n8, n9 = [], [], [], [], [], [], [], [], []

        else:
            i += 1
            nom = ''
            n1, n2, n3, n4, n5, n6, n7, n8, n9 = [], [], [], [], [], [], [], [], []

    else:
        i += 1
        nom = ''

print('result:', result)
