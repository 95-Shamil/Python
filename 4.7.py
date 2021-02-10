from itertools import count
from math import factorial
n = int(input('Введите начальное число '))

def fibo_gen():
    for el in count(n):
        yield factorial(el)


gen = fibo_gen()
x = 0
y = int(input('Число первых x чисел '))
for i in gen:
    if x < y:
        print(i)
        x += 1
    else:
        break
