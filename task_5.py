# Реализуйте алгоритм перемешивания списка.
import random
from time import time
n = int(input("Введите число N: "))
list = []
for i in range(0,n):
    list.append(int(random.randint(n*-1, n)))
print(list)

