n = int(input('ширина треугольника   '))
a = 1
i = '*'
j = ' '
while a <= n:
    print(j * (n - a), i * a)
    a += 1
