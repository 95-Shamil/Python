def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(
    f'Result - {my_func(int(input("Первый аргумент ")), int(input("Второй аргумент ")), int(input("Третий аргумент ")))}')
