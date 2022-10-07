# Напишите программу где пользователь вводит число symbol_len, а программа генерирует пароль длинной symbol_len.
# Чем выше будет сложность пароля, тем лучше. Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
import random

# symbol_len = int(input('Введите число  '))
# hidden_number = random.randint(range(1,symbol_len))
# print(symbol_len)
import random
import string
N = int(input('Введите число '))
allowedChars = string.ascii_letters + string.digits + string.punctuation
paroll = ''.join(random.choice(allowedChars) for _ in range(N))
print(paroll)

ascii_lowercase = 0
ascii_uppercase = 0
digits = 0
ispace = 0
special = 0
symbol = 0
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
    print('Уровень сложности: 1')
elif len(paroll) > 8 and ascii_uppercase > 0 and ascii_lowercase and special > 0 and digits > 0:
    print('Уровень сложности: 5')
elif ascii_uppercase > 0 and ascii_lowercase and digits > 0:
    print('Уровень сложности: 4')
elif ascii_lowercase > 0 and digits > 0:
    print('Уровень сложности: 3')
elif ascii_lowercase > 0 and ascii_uppercase > 0:
    print('Уровень сложности: 2')
else:
    print('Введите пароль заново')