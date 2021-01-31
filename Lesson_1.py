# Задание 1
a = 5
b = 3
print('Переменные a и b', a, b)
line_1 = input('Введите строку №1 ')
number_1 = int(input('Введите цифру №1 '))
line_2 = input('Введите строку №2 ')
number_2 = int(input('Введите цифру №2 '))
print('Вывод введенных значений: ', line_1, number_1, line_2, number_2)

# Задание 2
time = int(input('Время в секундах '))
hour = time // 3600
minute = (time - hour * 3600) // 60
seconds = time - (hour * 3600 + minute * 60)
print(f'Время в формате чч:мм:сс {hour} : {minute} : {seconds}')

# Задание 3
n = int(input('Ввод числа - '))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print('Сумма чисел - ', total)

# Задание 4
n = abs(int(input('Введите целое положительное число - ')))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break
# В задании 4 у меня возникла проблема с пониманием. Получилось с помощью ручки, бумаги, логики и перебора вариантов.
# Но я до сих пор не понимаю, почему программа понимает значение max в конце программы. Просьба объяснить

# Задание 5.
revenue = float(input('Выручка '))
COGS = float(input('Издержки '))
if revenue > COGS:
    print(f'Есть прибыль {revenue - COGS}. Рентабельность {revenue / COGS}')
    workers = int(input('Численность сотрудников '))
    print(f'Прибыль на сотрудника {revenue / workers}')
elif revenue == COGS:
    print('Выручка равна расходам, безубыточное производство')
else:
    print('У компании убыток')

# Задание 6

a = int(input('Первый день пробежки км - '))
b = int(input('Цель, км '))
days = 1
km = a
while km < b:
    a = a + 0.1 * a
    days = days + 1
    km = km + a
print('Результат будет достигнут на день', days)
