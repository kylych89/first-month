#PROBLEM 1
'''
a= 2**3
b = 3**2
if a > b:
    print(a)
elif a < b:
	print(b)
'''

'''
#PROBLEM 2
nums = int(input('Введите ваше число'))
if nums >= 0 and nums <= 21:
	print('Разрешенённые')
elif nums >= 57 and nums <= 100:
	print('Разрешенённые')
else:
	print('запрещёного')
'''

'''
#PROBLEM 3
nums = int(input('Введите ваше число: '))
if nums % 2 == 0:
	print('Чётное число: ', nums)
elif nums % 2 != 0:
	print('Нечётное число', nums)
if nums ** 2 and nums > 1000:
	print(nums)
else:
	print('< 1000')
'''

'''
#PROBLEM 4

data = int(input('Введите ваш возраст: '))
years = 18
if data >= years:
	print('За работу')
elif data <= years:
	print('Тебе еще рано')
else:
	print('Спасибо')
'''

'''
#PROBLEM 5
a = 10 // 5
b = 10 / 5
if a == b:
	print('Равны')
elif a != b:
	print(a)
	print(b)
	print('Не равны')
'''


'''
#PROBLEM 6
data = int(input('Введите число: '))
if data >= 0 and data <= 100:
	print(-data)
'''


'''
#PROBLEM 7
a = 10
b = 5
if a >= 0 and b >= 0:
	print('Положительные числа')
else:
	print('Отрицтельные числа')
'''

'''
#PROBLEM 8
a = 10
b = 5
if a > b:
	a += 2
	print(a)
else:
	b += 2
	print(b)
'''

'''
#PROBLEM 9
nums = int(input('Введите любое число: '))
if nums > 0:
	print('Положительное число')
elif nums < 0:
	print('Отрицательное число')
else:
	print(nums)
'''

'''
#PROBLEM 10
years = int(input('Введите ваш возраст: '))
if years >= 18:
	print('Совершеннолетний')
elif years <= 4:
	print('Ребенок')
else:
	print('Несовершеннолетий')
'''

'''
#PROBLEM 11
a = 45
b = 6
if a % b:
	print('Верно')
else:
	print('Не верно')
'''

'''
#PROBLEM 12
data = int(input('Введите любой год: '))
year = 2022
if data == year:
	print('Текущий год')
elif data > year:
	print('Год еще не наступил')
else:
	print('Год прошел')
'''

'''
#PROBLEM 13
years = int(input('Введите ваш возраст: '))
if years >= 18:
	print('Совершеннолетний')
elif years <= 4:
	print('Ребенок')
else:
	print('Несовершеннолетий')
'''

'''
#PROBLEM 14
a = 10
b = 15
c = 20
if a < b or b < c or a > b or b > c:
	print(c)
	print(a)
'''


'''
#PROBLEM 15
a = 17391
b = 546
c = 934
if a % b:
	print(a % 17)
elif b % a:
	print(b % 17)
elif c % a:
	print(c % 17)
'''


'''
#PROBLEM 16
x = 13
var = x ** 2
if x == 172:
	print(var)
elif x < 172:
	var += x
	print(var)
'''

'''
# Формула для вычисления идеального веса
pol = input('Введи букву M если ты мужчина, и букву W если ты женщина: ')
rost = int(input('Введи возраст: '))
r = 0
if pol == 'M':
	r = int(((rost * 4 / 2.5) - 128) * 0.458)
elif pol == 'W':
	r = int(((rost * 3.5 / 2.5) - 108) * 0.458)
print('Твой идеальный вес должен быть: ' + str(r))
'''

'''
#Погода в Бишкеке
pogoda = int(input('Введите цифру 1 или 2: '))
temp1 = 1
temp2 = 2
answer = ''
if pogoda == temp1:
	answer += 'Погода сейчас теплая в Бишкеке!'
	print(answer)
elif pogoda == temp2:
	answer += 'Сейчас погода холодно в Бишкеке!'
	print(answer)
'''

'''
#Проверка логина и пароля
login = input('Введите ваш логин: ')
password = int(input('Введите ваш пароль: '))

ivan = 'Ivan'
passwordIvan = 12345

marina = 'Marina'
passwordMarina = 123456

if login == ivan and password == passwordIvan or login == marina and password == passwordMarina:
	print('Добро пожаловать в инстаграм!!!')
else:
	print('Посылаю тебя неизвестного юзверя лесом!!!')
'''
