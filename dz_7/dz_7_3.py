import random
hidden_number = random.randint(1, 10)
for i in range(1,4):
    number = int(input('попытка #' + str(i)))
    if number > hidden_number:
        print('Много')
    elif number < hidden_number:
        print('Мало')
    else:
        print('Ты угадал')
else:
    print(f'Ты не угодал, загадано число {hidden_number}')
