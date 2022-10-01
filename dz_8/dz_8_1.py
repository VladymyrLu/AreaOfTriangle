 # 1/Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра. Если это так, то вывести 'YES', иначе 'NO'

test_string = input('введите стоку ')
ascii_lowercase = 0
ascii_uppercase = 0
digits = 0
ispace = 0
symbol = 0
for symbol in test_string:
    if symbol.isupper():
        ascii_uppercase += 1
    elif symbol.islower():
        ascii_lowercase += 1
    elif symbol.isdigit():
        digits += 1
    elif symbol.isspace():
        ispace += 1
    else:
        symbol += 1
if ascii_lowercase > 0 and ascii_uppercase > 0 and digits > 0 and ispace > 0:
    print('YES')
else:
    print('NO')

