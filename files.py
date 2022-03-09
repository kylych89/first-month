
#1 Задание
#names = 'bin  boot  cdrom  dev  etc  home  lib  lib32  lib64  libx32  lost+found  media  mnt  opt  proc  root  run  sbin  snap  srv  swapfile  sys  tmp  usr  var'

'''
f = open('/home/kylych/Рабочий стол/python files/directories.txt', 'w')
f.write(names)
f.close()
'''
'''
f = open('/home/kylych/Рабочий стол/python files/directories.txt', 'r')
r = f.read()
print(r)
f.close()
'''


'''
#2 Задание
login = input('Login: ')
password = input('Password: ')
with open('/home/kylych/Рабочий стол/python files/users.txt', 'w') as user:
	user.write('Логин:')
	user.write(login)
	user.write('\n')
	user.write('Пароль:')
	user.write(password)
'''


#3 Задание

t = '''
Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java.

'''


'''
f = open('/home/kylych/Рабочий стол/python files/find W.txt', 'w')
f.write(t)
f.close()
'''

'''
f = open('/home/kylych/Рабочий стол/python files/find W.txt', 'r')
for i in f.read():
	print(i, end=' ')
	if i == 'w':
		print('Да в тексте есть w')
if 'w' not in f.read():
	print('Нет, в тексте нет w')

f.close()
'''


#4 Задание

txt = '''
Python is a widely used high-level programming language for general
programming, created by Guido van Rossum and first released in 1991. An inter
language, Python has a design philosophy that emphasizes code readability (no
using whitespace indentation to delimit code blocks rather than curly bracket
keywords), and a syntax that allows programmers to express concepts in fewer
code than might be used in languages such as C++ or Java.
'''

'''
t_words = []

with  open('python.txt', 'r') as file:
	for i in file.read():
		if i == 't':
			t_words.append(i)

print(t_words)
'''


#5 Задание
'''
f = open('/home/kylych/Рабочий стол/python files/database.txt', 'w')
for i in range(3):
	f.write('\n')
	login = input('Login: ')
	f.write('Логин: ')
	f.write(login)
	f.write('\n')
	password = input('Пароль: ')
	f.write('Пароль: ')
	f.write(password)
	f.close()
print('file writed successfully!!!')
'''
'''
with open('/home/kylych/Рабочий стол/python files/database.txt', 'a+') as f:
    login = input('Введите логин: ')
    with open('/home/kylych/Рабочий стол/python files/database.txt', 'r') as r:
        data = [i for i in r.read().split()]
        while login in data:
            print('Такой логин уже есть введине новый')
            login = input('Введите логин: ')
    f.write('\n')
    f.write('Логин: ')
    f.write(login)
    f.write('\n')
    passwor = input('Введите пороль: ')
    passwor1 = input('Введите пороль повторно: ')
    while passwor != passwor1:
        print('Пороли не совпадают')
        passwor = input('Введите пороль: ')
        passwor1 = input('Введите пороль повторно: ')
    f.write('Пароль: ')
    f.write(passwor)
    f.write('\n')

    print('Успешно записан!')
'''



# 6 Задание
# 6 Задание
# try:
#     with open(f'{photo}', 'rb'):
#         print('Такой файл существует')
# except FileNotFoundError:
#     print('Введите кореектный файл')

# with open('task6.txt', 'w') as file:
    
#     login = input('Введите логин: ')
#     password = input('Введите пароль: ')
#     photo = input('Ваше фото пожалуйста: ')
#     try:
#         with open(f'{photo}', 'rb'):
#             print('Такой файл существует')
#             file.write('\n')
#             file.write('Логин: ')
#             file.write(login)
#             file.write('\n')
#             file.write('Пароль: ')
#             file.write(password)
#             file.write('\n')
#             file.write('Место для фото ')
#             file.write(photo)
#             print('Регистрация Успешна!')
#     except FileNotFoundError:
#         print('Введите кореектный файл')
#     finally:
#         print('ПРОГРАММА ЗАВЕРШЕНА')
    

# with open('task6.txt', 'r') as file:
#     for i in file.read().split():
#         print(i, end=" ")



# 7 Задание
'''
a = input("Путь до картинки которую нужно изменить: ")
b = input("Путь до картинки НА которую нужно изменить: ")
f1 = open("/home/kylych/python/firstMonth/photos/b805fc7a147082f3830e110807e34546.jpeg", "r")
f2 = open("/home/kylych/Загрузки/2100_thumbnail_Screenshot_2021_1200x768.jpeg", "r")
f3 = open("/home/kylych/Загрузки/b805fc7a147082f3830e110807e34546.jpeg", "a+")
try:
    if a and b:
        f3.write("/home/kylych/python/firstMonth/photos")
        print("Фотка успешно переписано")
    else:
        print("Такая картинка не существует")
except:
    print("Oshibka")
finally:
    f1.close()
    f2.close()
    f3.close()
'''


# 8 Задание

# 2 Monthes:
"""
January = 18000
February = 32641
March = 28300
April = 11200
May = 21100
June = 19000
July = 8000
August = 72000
September = 12300
October = 17000
November = 25000
December = 30000

f = open('D:\python txt files/monthes.txt', 'w')
f.write(str(January) + "\n")
f.write(str(February) + "\n")
f.write(str(March) + "\n")
f.write(str(April) + "\n")
f.write(str(May) + "\n")
f.write(str(June) + "\n")
f.write(str(July) + "\n")
f.write(str(August) + "\n")
f.write(str(September) + "\n")
f.write(str(October) + "\n")
f.write(str(November) + "\n")
f.write(str(December) + "\n")


f = open('D:\python txt files/monthes.txt', 'r')
summ = []
summ2 = []
read = f.read()
for i in read.split():
    summ.append(int(i))
    if summ[0] == 18000:
        summ2[0] = summ[0]
print(summ2)
print("ok")
f.close()
"""

# 9 Задание
"""
Создайте текстовый файл с целыми числами ->
Найти максимальное и минимальное число и записать в другой файл.
"""
"""
# a, b, c, d, i, f, j = 10, 45, 78, 98, 65, 32, 54
# with open('D:\python txt files/integer.txt', 'w') as file:
#     file.write(str(a) + "\n")
#     file.write(str(b) + "\n")
#     file.write(str(c) + "\n")
#     file.write(str(d) + "\n")
#     file.write(str(i) + "\n")
#     file.write(str(f) + "\n")
#     file.write(str(j) + "\n")

# with open('D:\python txt files/integer.txt', 'r') as file:
#     arr = []
#     read = file.read()
#     for i in read.split():
#         arr.append(int(i))
# with open('D:\python txt files/other_integer.txt', 'w') as fs:
#     print(max(arr), file=fs)
#     print(min(arr), file=fs)
"""


"""
Создайте текстовый файл ->
Записать в него построчно данные, которые вводит пользователь
Окончание ввода должен принимать пустую строку
"""
"""
f = open('D:\python txt files/txtFile.txt', 'a+')
a = input("Введите данные: ")
f.write(a)
f.write("\n")
f.write(a)
f.close()
"""
