# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# Пример
# 5 -> 1 0 1 1 0
# 2
import random

n = int(input('Введите количество монет '))
orel = reshka = 0

rand_list = []
for i in range(n):
    rand_list.append(random.randint(0, 1))
    if rand_list[i] == 0:
        reshka += 1
    else:
        orel += 1
    
if orel <= reshka:
    print(f'{n} -> {rand_list}')
    print(orel)
else:
    print(f'{n} -> {rand_list}')
    print(reshka)
