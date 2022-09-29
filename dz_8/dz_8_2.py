# 2/Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.

count = int(input("Введите число: "))
first = 0
second = 1
sum = 0
i = 1
print("Числа Фибоначчи: ")
while i <= count:
  print (sum)
  i += 1
  first = second
  second = sum
  sum = first + second
