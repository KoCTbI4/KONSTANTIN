import random
from collections import Counter

'''Первое задание. Создать массив из 100 целых чисел и вывести индекс элемента с нулевым значением'''
Mas = random.sample(range(101), 100)
#Mas = [39, 53, 76, 84, 90, 9, 45, 94, 2, 83, 4, 67, 40, 75, 31, 37, 58, 62, 44, 26, 92, 100, 18, 46, 0, 21, 86, 19, 7, 24, 79, 73, 22, 99, 93, 14, 6, 30, 48, 70, 68, 11, 3, 38, 89, 60, 17, 96, 34, 27, 41, 5, 1, 71, 88, 95, 32, 8, 98, 43, 47, 13, 64, 77, 49, 16, 91, 25, 69, 82, 33, 63, 20, 50, 35, 55, 10, 61, 81, 65, 74, 52, 57, 29, 85, 87, 12, 72, 42, 56, 78, 66, 80, 23, 54, 51, 97, 59, 15, 36]
print('Массив:\n', Mas)

for i,num in enumerate(Mas):

    if num == 0:

        print('Номер элемента с нулевым значением-',i)

'''Второе задание.В выше указанном массиве чисел, найдите наиболее часто встречающееся число в массиве. Если таких чисел несколько, определите наименьшее из них'''

Count_Mas = Counter(Mas)

#Проводится поиск минимального из максимально встречающихся чисел
most_common_number = min(
    [num for num, count in Count_Mas.items() if count == max(Count_Mas.values())]

)
print("Наиболее часто встречающееся и наименьшее из таких чисел:", most_common_number)




