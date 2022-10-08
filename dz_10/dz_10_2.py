X = int(input('Введите число  '))
Y = int(input('Введите число  '))
B = []

for j in range(Y):
    A = []
    for i in range(X):
        number = int(input(f'Enter number [{j}][{i}]: '))
        A.append(number)
    B.append(A)
print(B)

cols = list(list(row[i] for row in B) for (i, e) in enumerate(B[0]) if
    i % 2 and B[len(B) - 1][i] < e)
print(*cols)

