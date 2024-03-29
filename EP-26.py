'''Задача 26'''
# Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:
# 1/2	=	0.5
# 1/3	=	0.(3)
# 1/4	=	0.25
# 1/5	=	0.2
# 1/6	=	0.1(6)
# 1/7	=	0.(142857)
# 1/8	=	0.125
# 1/9	=	0.(1)
# 1/10=	0.1
# Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры.
# Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.
# Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся
# последовательность цифр.

result = 0
d = 0

for i in range(2, 1000):
    mod = 1
    index = 0
    nums = []
    while True:
        if mod % i == 0:
            break
        elif mod in nums:
            break
        nums.append(mod)
        mod = (mod * 10) % i
        index += 1
    if index > result:
        result = index
        d = i

print(d)