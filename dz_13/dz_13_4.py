def read_last(lines, file):
    if lines > 0:
        with open(file) as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print('только положительное число')

read_last(2, 'spisok.txt')
read_last(-1, 'spisok.txt')
