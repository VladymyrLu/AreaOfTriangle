
# Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на
# некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом вправо на 3, А была
# бы заменена на Г, Б станет Д, и так далее. Нужно реализовать шифрование с помощью Python.
# Пользователь вводит строку которую хочет зашифровать и число (сдвиг), нужно с помощью шифра Цезаря ее зашифровать и
# вывести на экран.#
# Выполнить задание нужно с помощью цикла for и строк, для получения числового представления символа можно использовать
# ord, а для преобразования числа в строку - chr..

smeshenie = int(input('введите сдвиг: '))
message = input("введите строку: ")
encryption = ""
for c in message:
    if c.isupper():
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        new_index = (c_index + smeshenie) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        encryption = encryption + new_character
    elif c.islower():
        c_unicode = ord(c)
        c_index = ord(c) - ord("a")
        new_index = (c_index + smeshenie) % 26
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)
        encryption = encryption + new_character
    elif c.isdigit():
        c_unicode = (int(c) + smeshenie) % 10
        encryption += str(c_unicode)
    else:
        encryption += c
print(f'шифровка {encryption}')
