number = 15
# print(number <= 10)
# print(1 <= number <= 15)
# print('ll' in 'Hello')
#
#
# if password == '123' and 'Vasya' in 'Vasya@gmail.com':
#     print(f'Hello Vasya@gmail.com')
# if password == '123' and 'Vasya' in 'Vasya123@gmail.com':
#     print(f'Hello Vasya123@gmail.com')

# number = 1
#
# if number == 1:
#     print('Переменная number равна 1')
#
# print('Конец программы')


# number = 3
#
#
# if number == 1:
#     print('Переменная number равна 1')
# elif number == 2:
#     print('Привет')
# else:
#     print('Переменная number имеет другое значение')
#
# print('Конец программы')

# number = 23
# guess = int(input('Введите целое число : '))
#
# if guess == number:
#     print('Поздравляю, вы угадали,')  # Начало нового блока
#     print('(хотя и не выиграли никакого приза!)')  # Конец нового блока
# elif guess < number:
#     print('Нет, загаданное число немного больше этого.')  # Ещё один блок
#     # Внутри блока вы можете выполнять всё, что угодно ...
# else:
#     print('Нет, загаданное число немного меньше этого.')
#     # чтобы попасть сюда, guess должно быть больше, чем number

# number = int(input('Enter number: '))
#
# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')
#
# is_even = 'Even' if number % 2 == 0 else 'Odd'
#
# print('Even' if number % 2 == 0 else 'Odd')

# number = 3
# condition = False
#
# if number % 2 == 0:
#     print(10)
# else:
#     if condition:
#         print(20)
#     else:
#         print(30)
#
# print(10) if number % 2 == 0 else print(20) if condition else print(30)

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# number = int(input('Enter number: '))
#
# while not 0 <= number <= 10:
#     print('Ошибка!')
#     number = int(input('Enter number: '))
#
# print('Получили правильное число!')


# while True:
#     number = int(input('Enter number: '))
#
#     if 0 <= number <= 10:
#         break
#
#     print('Ошибка')
#
# print('Получили правильное число!')

# number = 0
#
# while number != 100:
#     number += 1
#
#     if number % 2 != 0:
#         continue
#
#     print(number)


print('Конец цикла!')


number = 0

while number < 49:
    number += 3

    if number == 50:
        break

    print(number)

else:
    print('Цикл завершился успешно!')


print('Конец цикла!')


"""
1) Пользователя вводит два числа A и B, нужно вывести сумму чисел в диапазоне от A до B.
2) Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.
3) Пользователь вводит два числа A и B, нужно вывести прямоугольник со сторонами A и B с помощью символа '*' используя цикл.
В коде можно использовать символ '*' только один раз.
4) Запросить у пользователя число N, вывести треугольник шириной N используя символ '*'.
Input:
N = 6
Output:
******
*****
****
***
**
*
"""

















"""
1) Запросить у пользователя число N, вывести все числа от 0 до N которые делятся на 3.
"""


# N = int(input('Enter number: '))
# number = 0

# while number < N:
#
#     if number % 3 == 0:
#         print(number)
#
#     number += 1


# while number < N:
#     print(number)
#     number += 3























