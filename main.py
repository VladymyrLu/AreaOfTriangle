# A = int(input('Введите число А: '))
# B = int(input('Введите число B: '))
# sum = 0
#
# while A < B:
#     sum = sum + A
#     A += 1
# print (sum)

# A = int(input('Введите число А: '))
# B = int(input('Введите число B: '))
# sum = 0
#
# while A < B:
#     sum = sum + A
#     A += 1
#     if sum % 2 != 0:
#         continue
#     print (sum)

A = int(input("A  "))
B = int(input('B  '))
sum = 0
while  A < B:
    A += 1
    if A % 2 != 0:
        continue

    print(A)

n = int(input('ширина треугольника   '))
a = 1
i = '*'
    while a <= n:
        print(i * a)
    a += 1





















