# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max). Вывести эти числа.
N = int(input('число  '))
A = []
for i in range(0, N):
    number = int(input(f'число # {i + 1} '))
    A.append(number)
print(A)

Max = A[0]
Min = A[0]
for i in range(N):
    if A[i] > Max: Max = A[i]
    if A[i] < Min: Min = A[i]
print('Max:', Max, 'Min:', Min)
