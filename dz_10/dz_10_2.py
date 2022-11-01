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

for j, k in enumerate(B):
    for i, e in enumerate(k):
        if i % 2 == 0 and B[0][i] > B[(len(B)-1)][i]:
            print(e, end=' ')
    print('')


