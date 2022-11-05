class Notebook:
    def __init__(self):
        self.note = {}

    def add_person(self, key, vol):
        self.note[key] = vol
        return 'ok'

    def find(self, name):
        for _ in self.note:
            data = ' '.join(self.note[name])
            return f'{name} {data}'
        return 'Запись не найдена'

    def del_name(self, name):
        if name in self.note:
            del self.note[name]
            return f'{name} удалена'
        return 'нет такой в списке'

    def info(self):
        return self.note.items()



print('Записная книжка')
print('''Выберите пункт:
1 - Добавить запись
2 - Поиск по имени
3 - Удалить запись
4 - Просмотреть записи
5 - Выход''')


book = Notebook()

while True:
    print("Введите команду: \n")
    command = input()
    if command == '1':
        nam = input('Имя: ')
        fio = input('Фамилия: ')
        born = input('Дата рождения: ')
        address = input('Адресс: ')
        num = input('Номер телефона: ')
        print(book.add_person(nam, [fio, born, address, num]))
    elif command == '2':
        name = input('Введите имя, которое хотите найти >:  ')
        print(book.find(name))
    elif command == '3':
        name = input('Введите фамилию, которую хотите удалить >:  ')
        print(book.del_name(name))
    elif command == '4':
        for name, data in book.info():
            data = ' '.join(data)
            print(name, data)
    elif command == '5':
        exit()

    else:
        print('неизвестная команда')
    import pickle
    f = open('dz_15.txt', 'wb')
    pickle.dump(book, f)
    f.close()

