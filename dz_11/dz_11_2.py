files = {}
for i in range(int(input('количество файлов '))):
    name, *operations = input().split()
    files[name] = operations
for i in range(int(input('количество запросов '))):
    operation, name = input().split()
    if operation == 'read':
        if 'R' in files[name]:
            print('OK')
        else:
            print('Access denied')
    elif operation == 'write':
        if 'W' in files[name]:
            print('OK')
        else:
            print('Access denied')
    elif operation == 'execute':
        if 'X' in files[name]:
            print('OK')
        else:
            print('Access denied')
