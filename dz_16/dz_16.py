class Human:

    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return self.name, self.surname, self.age, self.phone, self.address

    def call_phone_number(self):
        return self.phone

Ivanov = Human('Ivan', 'Ivanov', 30, '050528658', 'Kiev')
Sosho = Human('Sasha', 'Sosho', 50, '095258500', 'Harkov')
Vovan = Human('Vova', 'Vovan', 25, '050528658', 'Kiev')

print(Ivanov.get_info())
print(Sosho.get_info())
print(Vovan.get_info())

print(Ivanov.call_phone_number())
print(Sosho.call_phone_number())
print(Vovan.call_phone_number())

#   def print_id(self):
#         self.file.write(f'{self.name} - {hex(id(self))}')
#         print(f'{self.name} - {hex(id(self))}')
#
#     def print_hobbies(self):
#         self.print_id()
#         print(f'{self.name} likes ')
#         print('\n'.join(self.hobbies))
#
# print(f'Lists: {Person.instance_count}')
# tom = Person('Tom', 25, 'Tennis, football, TV')
# bob = Person('Bob', 30, 'YouTube, Music')
#
# print(f'Lists: {Person.instance_count}')