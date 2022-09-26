import random
hidden_number = random.randint(1, 10)
i = 1
while i <= 3:
    number = int(input('попытка #' + str(i)))
    if number > hidden_number:
        print('Много')
    elif number < hidden_number:
        print('Мало')
    else:
        print('Ты угадал')
        break
    i += 1
else:
    print('Ты не угодал, загадано число', hidden_number)
