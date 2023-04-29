# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# Пример
# 10 -> 1 2 4 8

n = abs(int(input('Введите число n: ')))
count = 0
num = 2
for i in range(n):
    if count != 1:
        num = num ** i
        if num <= n:
            print(num, end=" ")
            num = 2
        else:
            count = 1
    else:
        i = n
