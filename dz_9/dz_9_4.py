# Задание 4:
# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности
N = int(input('число  '))
A = []
for i in range(0, N):
    number = int(input(f'число # {i + 1} '))
    A.append(number)
print(A)
print(list(reversed(A)))
