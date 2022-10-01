import \
    string  # 3/Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и выводит свой результат в оценочной шкале от 1 до 5.
# 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
# 2 - у пользователя все буквы в нижнем регистре
# 3 - у пользователя есть буквы в нижнем регистре и цифры
# 4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
# 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов

paroll = input('введите стоку ')
ascii_lowercase = 0
ascii_uppercase = 0
digits = 0
ispace = 0
special = 0
symbol = 0
import string
for symbol in paroll:
    if symbol.isupper():
        ascii_uppercase += 1
    elif symbol.islower():
        ascii_lowercase += 1
    elif symbol.isdigit():
        digits += 1
    elif symbol.isspace():
        ispace += 1
    elif symbol in string.punctuation:
        special += 1
    else:
        symbol += 1
if 'qwerty' == paroll or 'admin' == paroll or '' == paroll:
    print('1')
elif len(paroll) > 8 and ascii_uppercase > 0 and ascii_lowercase and special > 0 and digits > 0:
    print('5')
elif ascii_uppercase > 0 and ascii_lowercase and digits > 0:
    print('4')
elif ascii_lowercase > 0 and digits > 0:
    print('3')
elif ascii_lowercase > 0:
    print('2')
else:
    print('Введите пароль заново')