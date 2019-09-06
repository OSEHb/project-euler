'''Задача 40.'''
# Дана иррациональная десятичная дробь, образованная объединением положительных целых чисел:
# 0.123456789101112131415161718192021...
# Видно, что 12-ая цифра дробной части - 1.
# Также дано, что dn представляет собой n-ую цифру дробной части. Найдите значение следующего выражения:
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

nom = '0.'
result = 1
lennom = 0

for i in range(1, 1000001):  # Время работы 6,6 с
    nom += str(i)

nom = nom[2:]

for j in nom:
    lennom += 1

    if lennom == 1 or lennom == 10 or lennom == 100 or lennom == 1000 or lennom == 10000 or lennom == 100000 \
            or lennom == 1000000:
        result *= int(j)

print('result:', result)
