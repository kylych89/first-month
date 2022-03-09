# list1= [1,3,[2,46,78,[True, False , ['hello',['feliks'], 'ravil'], 'dima']]]

# s = []
# def recurs(list1):
#     for i in list1:
#         if type(i) == list:
#             recurs(i)
#         else:
#             s.append(i)


# print(s)

# recurs(list1)

# print(s)


# # for i in list1:
# #     if type(i) == list:
# #         for j in i:
# #             if type(j) == list:
# #                 for k in j:
# #                     if type(k) == list:
# #                         for p in k:
# #                             s.append(p)
# #                     else:
# #                         s.append(k)
# #             else:
# #                 s.append(j)
# #     else:
# #         s.append(i)


# s = 0

# def minus(s):
#     if s != 20:
#         print(s)
#         s += 1
#         minus(s)
# minus(s)



# print((lambda x,y: x * y )(2,8))

# def artem(kiri):
#     def beknazar():
#         print("<\___i am artem___/>")
#         kiri()
#         print("<\___i am not artem___/>")
#     return beknazar

# def ravil(kiri):
#     def beknazar():
#         print("<\___hello___/>")
#         kiri()
#         print("<\___end___/>")
#     return beknazar

# @artem
# @ravil
# def aktan():
#     print(564656+65456465456)
# aktan()




# Написать lambda которая принимает 3 параметра и умножает все параметры между собой.
# Функция должна вернуть строку: "Объём бассейна " и значение которое получилось
# print((lambda x, y, z: f'Объём бассейна {x * y * z}') (5, 4, 9))


# Написать lambda которая получает сколько дней ПРОШЛО с нового года 
# как параметр и говорит пользователю сколько дней ОСТАЛОСЬ до нового года
# print((lambda x, y: f'дней ОСТАЛОСЬ до нового года {y-x}')(54,365))


# Напишите программу которая выводит только нечётные числа с помощью рекурсии
# def odd_numbers(number1):
#     if number1 % 2 != 0:
#         print(number1)
#     number1 += 1
#     if number1 == 45:
#         return number1
#     odd_numbers(number1)
# odd_numbers(1)



# Напишите функцию которая принимает SET и рекурсивно удаляет оттуда 
# по одному элементу при запуске
# def sets(set1):
#     if len(set1) == 0:
#         return set1
#     print(set1)
#     set1.pop()
#     sets(set1)
# s = {1,2,3,4,5,6}
# sets(s)



# Напишите функцию которая генерирует 100 рандомных чисел 
# в диапазоне от 10 до 50 и возвращает их в листе.
# Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты 
# в первой функции и вернёт всё так же лист
# import random
# def gen_random(func):
#     def self():
#         print('start')
#         ls = func()
#         print(list(set(ls)))
#         print('end')
#     return self

# @gen_random
# def decor(): 
#     ls = []
#     for i in range(100):
#         r = random.randint(10, 50)
#         ls.append(r) 
#     print(ls)
#     return ls

# decor()



# 24.02.2022
# Напишите функцию которая спрашивает у пользователя login и password.
# Напишите декоратор который шифрует эти данные и возвращает вам зашифрованные данные.
# (Можете воспользоваться функцией ord и char, можете загуглить...)
# from werkzeug.security import generate_password_hash
# def hash_code(ask_login_password):
#     def self(login, password):
#         log = generate_password_hash(login)
#         has = generate_password_hash(password)
#         ask_login_password(log, has)
#         print('логин после шифровки:', log)
#         print('пароль после шифровки:', has)
#     return self


# @hash_code
# def ask_login_password(login, password):
#     return login, password

# login = input("Введите логин: ")
# password = input("Введите пароль: ")
# ask_login_password(login,password)


# second way with ord and char
# def hash_ord_char(func):
#     def wrapper(login, password):
#         log = ''.join(str(ord(i)) for i in login)
#         return  log , chr(password)
#     return wrapper

# @hash_ord_char
# def ask_login_password(login, password):
#     return login, password

# login = input("Введите логин: ")
# password = int(input("Введите пароль: "))
# print(ask_login_password(login, password))



# Создайте lambda функцию которая принимает одно число и возвращает это число умноженное на 1.185
# Вам дан список [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
# пройдите по списку и примените функцию к каждому числу
# ls = [1745345, 98726, 439872634, 7312, 64872, 123687126, 9312, 4124, 231, 3123, 34, 3453]
# for i in ls:
    # x = 1.185
    # print((lambda x, i: x*i)(x, i))
    # print((lambda i: (i * 1.185))(i))



# def team(func):
#     def wrapper(a, b):
#         print("hello")
#         func(a, b)
#         print("bye")
#     return wrapper


# @team
# def ok(a, b):
#     print("continue", a * b)


# ok(10, 10)