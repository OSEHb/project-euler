'''Задача 14.'''
# Следующая повторяющаяся последовательность определена для множества натуральных чисел:
# n → n/2 (n - четное)
# n → 3n + 1 (n - нечетное)
# Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов. Хотя это до сих пор и не доказано
# (проблема Коллатца),предполагается,что все сгенерированные таким образом последовательности оканчиваются на 1.
# Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?
# Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.

num = 1
table = {}
result = []
for i in range(1, 1000000):  # Время работы 1,5 мин
    wey = [i, ]
    while True:
        if num == 1:
            n = len(wey)
            result.append(n)
            table[n] = i
            num += i
            wey = []
            break
        if num % 2 == 0:
            num //= 2
            wey.append(num)
            continue
        if num % 2 != 0:
            num = num * 3 + 1
            wey.append(num)

key = max(result)
print(table[key])