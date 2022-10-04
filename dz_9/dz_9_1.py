# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список


A = []
for i in range(0, 5):
    number = int(input(f'число # {i + 1} '))
    A.append(number)
print(A)
