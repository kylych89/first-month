
# import platform, random, secrets, string

# print("Platforma: ", platform.architecture())

# print("Proses: ", platform.processor())
# print("mashina: ", platform.machine())

# a = string.digits + string.ascii_letters
# password = ''.join(secrets.choice(a)) 
# for i in range(16):
#     print(password)

# token = secrets.token_hex(16)
# print(token)

# print(random.random())
# print(random.randint(3, 10))


# farm_2 = ["cow", "horse", "donkey", "cat", "dog"]
# print(random.choice(farm_2))

# from random import shuffle


# shuffle(farm_2)
# print(farm_2)

# import datetime

# start = datetime.datetime.now()

# for i in range(10):
#     print(i)
#     print(datetime.datetime.now() - start)


# import os

# print(os.name)




# task 1
# a = "Я функция из my_module.py"
# print(a)




# task 2
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# names2 = []
# for i in names:
#         names2.append(random.choice(names))
#         if len(names2) == 4:
#             break
# print(names2)




# task 3
# import sys
# print(sys.platform)


# task 5
# import random, os
# os.mkdir('first_modules')
# i = 0
# while i < 4:
#     a = random.randint(1,50)
#     os.mknod(f'/home/kylych/python/firstMonth/first_modules/{a}.txt')
#     i += 1
# print(a)


# task 6
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek",
#          "Dastan", "Maksat"]
#
# first = []
# second = []
# third = []
# fourthd = []
#
# for i in names:
#     first.append(random.choice(names))
#     if len(first) == 3:
#         continue
#     second.append(random.choice(names))
#     if len(second) == 3:
#         continue
#     third.append(random.choice(names))
#     if len(third) == 3:
#         continue
#     fourthd.append(random.choice(names))
#     if len(fourthd) == 3:
#         break
#
# print("Первая команда", first)
# print("Вторая команда", second)
# print("Третья команда", third)
# print("Четвертая команда", fourthd)


# task 7

# import sys

# a = input(sys.argv)
# b = []
# b.append(a)
# print(b)


# task 8
# import sys

# a = input("1: ")
# b = input("2: ")
# if a > b:
#     print(sys.getsizeof(a))
# if a < b:
#     print(sys.getsizeof(b))

# task 9
# import random
#
# a = int(input("Введите число для генерации пароля: "))
# print(random.getrandbits(a))

# task 10
# import random
#
# i = 0
# while i == 0:
#     player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
#     if player == 1 or player == 2 or player == 3:
#         i = 1
#     if player == 1:
#         print("Вы выбрали камень.")
#     if player == 2:
#         print("Вы выбрали ножницы.")
#     if player == 3:
#         print("Вы выбрали бумагу.")
#     comp = random.randint(1, 3)
#     if comp == 1:
#         print("Компьютер выбрал камень.")
#     if comp == 2:
#         print("Компьютер выбрал ножницы.")
#     if comp == 3:
#         print("Компьютер выбрал бумагу.")
#     # определяем победителя
#     if player == comp:
#         win = 0
#     if player == 1 and comp == 2:
#         win = 1
#     if player == 1 and comp == 3:
#         win = 2
#     if player == 2 and comp == 1:
#         win = 2
#     if player == 2 and comp == 3:
#         win = 1
#     if player == 3 and comp == 1:
#         win = 1
#     if player == 3 and comp == 2:
#         win = 2
#     if win == 0:
#         print("Ничья!")
#     if win == 1:
#         print("Победил игрок!")
#     if win == 2:
#         print("Победил компьютер!")


# task 11

# import random
# print(random.randrange(6, 12))
# print(random.randrange(5, 100))

# task 12


# task 13
# import datetime
#
# dateTimeNow = datetime.datetime.now()
# dateTimeAfter = datetime.timedelta(days=1000)
# result = dateTimeNow + dateTimeAfter
# print("через 1000 дней от текущей даты:", result)


# ПОВТОРЕНИЕ:
# ЗАДАНИЕ 1:
# NUMBERS = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# summ = 0
# for i in NUMBERS:
#     summ += i
# print(summ)


# ЗАДАНИЕ 2:
# В PYTHON ЕСТЬ МОДУЛЬ DATETIME А В МОДУЛЕ ЕСТЬ ОСОБЕННЫЕ ФУНКЦИИ КОТОРЫЕ ПОКАЗЫВАЮТ НАСТОЯЩЕЕ ВРЕМЯ.
# С ПОМОЩЬЮ МОДУЛЯ DATETIME ВЫВЕДИТЕ НА ЭКРАН СКОЛЬКО ВРЕМЕНИ В ДАННЫЙ МОМЕНТ.
# import datetime
# print(datetime.datetime.now())


# ЗАДАНИЕ 3:
# В PYTHON ЕСТЬ МОДУЛЬ TIME, С ПОМОЩЬЮ НЕГО МОЖНО ОТПРАВЛЯТЬ ПРОГРАММУ В СОН.
# ЗАПУСТИТЕ ЦИКЛ FOR I IN RANGE(10) И КАЖДЫЙ ШАГ ЦИКЛА ВЫЗЫВАЙТЕ ФУНКЦИЮ МОДУЛЯ TIME КОТОРАЯ ЗАСТАВЛЯЕТ ПРОГРАММУ ЗАСНУТЬ.
# import time
# for i in range(10):
#     print(time.sleep(i))


# ЗАДАНИЕ 4:
# В PYTHON ЕСТЬ ВСТРОЕННАЯ ФУНКЦИЯ КОТОРАЯ ПОЗВОЛЯЕТ ОБЪЕДИНЯТЬ ДВА СПИСКА ДЛЯ ЦИКЛА FOR.
# ЗАПУСТИТЕ ЦИКЛ FOR С ДВУМЯ ПЕРЕМЕННЫМИ КОТОРЫЕ БУДУТ ПРОХОДИТЬ ПО LIST1 И LIST2 ОДНОВРЕМЕННО И ВЫВОДИТЕ ЭТИ ПЕРЕМЕННЫЕ НА ЭКРАН
# LIST1 = [1, 3, 5, 7, 9, 11, 13]
# LIST2 = [2, 4, 6, 8, 10, 12, 14]
#
# for x, y in zip(LIST1, LIST2):
#     print(x)
#     print(y)


# Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой
# def dict_appender(dic1, dic2):
#     dic1.update(dic2)
#     print(dic1)
#
# dic1 = {1: 'python'}
# dic2 = {2: 'java'}
# dict_appender(dic1, dic2)


# Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить.
# А затем записывает это всё в файл на рабочем столе menu.txt
# def order_eat(order):
#     with open("C:\\Users\\Sayfullah\\Desktop\\menu.txt", "w") as file:
#         file.write(order)
#     print("Success!!!")
#
# eat_and_drink = input("чтобы вы хотели заказать покушать и выпить: ")
# order_eat(eat_and_drink)


# Создайте функцию которая принимает слово и создаёт файл с таким именем в той же директории,
# где был запущен Ваш .py файл.
# def write_word(word):
#     file = open("pythonProject.txt", "w")
#     file.write(word)
#     file.close()
#     print("success!!!")
#
# write_word("kylych")


# Создайте 2 функции где одна функция вложена в другую.
# Главная функция должна выводить на экран текст: "Я главная функция".
# А вложенная функция должна выводить на экран: "Я вложенная функция."
# def nested_func():
#     print("Я вложенная функция")
#
#
# def main_func():
#     print("Я главная функция")
#     nested_func()
#
#
# main_func()


# Создайте функцию которая принмает тип данных dictionary,
# но возвращает два Tuple в одном из них все ключи,
# в другом только значения.
# def dict(dict):
#     tup1 = (1, 2, 3)
#     tup2 = ("python", "java", "php")
#     return tup1, tup2
#
#
# dic = {1: 'python'}
# print(dict(dic))


# Напишите программу которая определяет ПРОСТЫЕ ЧИСЛА.
# Простое число - это число которое делится только на себя и на 1.
# def prime(number):
#     n = number
#     counter = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             counter += 1
#     return 'Простое число' if counter == 2 else 'Составное число'
#
#
# print(prime(3))


# Напишите функцию которая принимает 2 аргумента.
# Эти аргументы могут быть любого типа данных но функция должна
# Вам вернуть эти аргументы как тип данных List.
# def any_args(*args):
#     ls = [args]
#     args = ls
#     return args
#
#
# print(any_args(1, 2, 3))


# Напишите функцию которая спрашивает у пользователя число
# и выводит ему на экран именно столько строк самой себя как текст.
# def ask_number(number):
#     st = "a"
#     for i in range(number):
#         st += str(i)
#     print(st)
#
# ask_number(5)


# Создайте функцию которая принимает Имя пользователя и его зарплату и возвращает это строкой как:
# ИМЯ - ЗАРПЛАТА.Если в функции не была указана зарплата - подставьте её сами.
# Значение по умолчанию - 5000.
# def name_salary(name, salary=5000):
#     print("ИМЯ:", name, "ЗАРПЛАТА:", salary)
#
#
# name_salary("kylych")


# Напишите функцию которая спрашивает число N и генерирует вам List состоящий из N разных элементов.
# def gen_number(number):
#     ls = []
#     import random
#     number = random.randint(1, 10)
#     ls.append(number)
#     return ls, number
#
#
# print(gen_number(5))



# n = 16
# k = n - 1
# for i in range(0, n):
#         for j in range(0, k):
#                 print(end=" ")
#         k -= 1
#         for j in range(0, i+1):
#                 print("*", end=" ")
#         print("*/*|*\*/*|*\*|*/*\\*/*|*\*/*|*\*|*/*\\*/*|*\*/*|*\*|*/*\\*/*|*\*/*|*\*|*/*\\")


# for i in range(15):
#     if i < 5:
#         print('|*                              *|                                                                     *\r')
#     if i == 5:
#         print('|*        ***********           *|                               *****************                     *')
#     if i >5 and i<12:
#         print('|*        *         *           *|                               *               *                     *\r')
#     if i ==12 :
#         print('|*        *         *           *|                               *****************                     *\r')
    
#     if i >11:
#         print('|*        *         *           *|                                                                     *\r')
     
#     if i==14:
#         print('********************************************************************************************************')