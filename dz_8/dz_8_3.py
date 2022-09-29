 # 3/Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и выводит свой результат в оценочной шкале от 1 до 5.
# 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
# 2 - у пользователя все буквы в нижнем регистре
# 3 - у пользователя есть буквы в нижнем регистре и цифры
# 4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
# 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов

# paroll = input('Введите пароль  ')
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
# if 'qwerty' == paroll or 'admin' == paroll or '' == paroll:
#     print('1')
# elif paroll == ascii_lowercase:
#     print('2')


p = input(("plz enter a password to check it's strength"))

upper_case = 0
lower_case = 0
number = 0
symbol = 0

for i in p:
    if i.isupper():
        upper_case += 1
    elif i.islower():
        lower_case += 1
    elif i.isdigit():
        number += 1
    else:
        symbol += 1

if len (p) <= 6:
    print("This is a weak password  ")
elif upper_case > 0 and lower_case > 0 and number > 0 and symbol > 0:
    print ("Good")
else:
    print ("Too Weak")