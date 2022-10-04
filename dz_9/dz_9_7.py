# Задание 7:
# Пользователь вводит текст нужно вывести количество цифр в этом тексте
# Пример:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Количество цифр: 3

text = input('Введите строку ')
num = [int(i) for i in text if i.isdigit()]
print('Количество цифр в тексте:', len(num))















# x = len([i for i in input() if i.isdigit()])
# # print(x if x else 'нет цифр в строке')
#
# line=input("")
# cnt=0
# for s in line:
#     if s.isdigit():
#         cnt+=1
# if cnt:
#     print(cnt)
# else:
#     print("числа не обнаружены")
#
