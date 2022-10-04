# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C
A = []
for i in range(0, 5):
    number = int(input(f'число # {i + 1} '))
    A.append(number)
print('Список А: ', A)

C = []
for c in A:
    if c > 5:
        C.append(c)
print('Список С: ', C)




