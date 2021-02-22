my_list = [3, 5, 5, 6, 7, 6, 6, 3, 2, 1]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)


