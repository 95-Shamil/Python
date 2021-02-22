my_list = [30, 5, 6, 7, 2, 4, 5, 12]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Первый вариант {my_list}')
print(f' Второй вариант {my_new_list}')
