def div(*args):
    try:
        arg1 = int(input("Делимое "))
        arg2 = int(input("Делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return "На нуль делить нельзя!"

    return res


print(f'result  {div()}')
