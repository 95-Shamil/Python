from itertools import count

for el in count(int(input('Первое число '))):
    print(el)

from itertools import cycle

my_list = [25, 'Python', 'Privet', 95]
for el in cycle(my_list):
    print(el)
