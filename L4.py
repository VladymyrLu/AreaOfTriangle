# number = 11

# print(number <= 10)
# print(1 <= number <= 15)
# print('ll' in 'Hello')
#
#
# if password == '123' and 'Vasya' in 'Vasya@gmail.com':
#     print(f'Hello Vasya@gmail.com')
# if password == '123' and 'Vasya' in 'Vasya123@gmail.com':
#     print(f'Hello Vasya123@gmail.com')


# if number == 11 :
#     print('ravno 11')
# else:
#     print('????')
# print('end')


number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Поздравляю, вы угадали,')  # Начало нового блока
    print('(хотя и не выиграли никакого приза!)')  # Конец нового блока
elif guess < number:
    print('Нет, загаданное число немного больше этого.')  # Ещё один блок
    # Внутри блока вы можете выполнять всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')
    # чтобы попасть сюда, guess должно быть больше, чем number