n = int(input('ширина треугольника   '))
a = 0
i = '*'
j = ' '
while a <= n:
    print(j * a, (n - a) * i)
    a += 1
