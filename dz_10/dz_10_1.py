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

print(*[x[0] for x in B])
print(*[x[-1] for x in B])




