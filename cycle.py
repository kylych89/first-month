'''
print(list(range(0,10, 2)))
a=[i for i in range(0,10,2)]
print(a)

i = 0
while i<3:
    i+=1
    print(i)
while True:
    s = input('How are you?')
    print(s)
    if s == 'yes':
        continue
    elif s == 'fine':
        break
'''


'''
while True:
    a = int(input('first number:'))
    c = input('operator')
    b = int(input('second number: '))
    if c == '+':
        print(a+b)
    if c == '-':
        print(a-b)
    if c == '*':
        print(a*b)
    if c == '/':
        print(a/b)
    s = input('can you continue?(yes/no)')
    if s == 'yes':
        continue
    elif s == 'no':
        break
'''

'''
i = 0
while i<3:
    a = {input('Name: '): input('work: ')}
    b = {'Рад знакомству: {}'.format(x): 'Крутая профессия {}'.format(y) for (x,y) in a.items()}
    print(b)
    i += 1
'''


'''
for i in range(1,50):
    if i % 2 == 0:
        print(i)
'''

'''
a = ['Бегимай', 'Akhmad', 'Кылыч', 'Актан', 'Аскар', 'Равиль', 'Илим']
s = []
for i in range(len(a)):
    if a[i] == 'Akhmad':
        continue
    print(i, a[i])
'''


'''
for i in 'hello world'.split():
    if i== 'o':
        continue
    print(i)
'''



'''
1. Допустим у нас есть список языков программирования.
Обязательное условие: если переменная в списке, то нужно вывести на экран 'this languages is in list'.
Если этого языка нет в списке, ничего не нужно выводить.
'''

'''
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for i in languages:
	if i == lang1:
		print('this languages is in list')
'''

'''
2. Будем работать с тем же списком:
С помощью цикла нужно “перебрать” все языки в списке, и когда код доходит до “php”, цикл должен быть прерван.
'''
'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	if i == 'php':
		print(i)
		break
'''


'''
3. Напишите код, который берёт цифру 7, умножает саму на себя же 5 раз.
'''
'''
a = 7
i = 0
while i <= 5:
	b = a ** i
	print(b)
	i += 1
'''

'''
4. Напишите код, который выведет на экран список языков с нумерацией.
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
Вывод:
0 go
1 java
2 php
3 python
4 javascript
5 ruby
'''
'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in range(len(languages)):
	print(i,languages[i])
'''



# 5. Напишите цикл который выведет на экран: 1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1
# Усиление:
# Получите такой же результат но с ОДНИМ циклом
'''
i = 0
j = 10
while i < 10:
    i += 1
    j -= 1
    print(i, end=',')
    print(j)
'''

# 6. У вас есть список имён:
# Если первое имя = 0, второе имя = 1 и т.д.
# Выведите на экран всё имена которые лежат на чётных числах
"""
names = (
'Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат',
'Аслан',)
index = 0
for i in range(len(names)):
    if i % 2 == 0:
        print(names[i], end=',')
"""

# 7. У вас всё тот же список имён:
# Выведите каждое 2 имя.
# Подсказка: Всего имён 13.
'''
names = (
'Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат',
'Аслан',)
for i in range(len(names)):
    if i % 2 == 1:
        print(i, names[i])
'''

# 8. Есть переменная которая хранит в себе число:
# Необходимо написать следующие условия для проверки переменной:
# 1. Это число трёхзначное?
# 2. Это число положительное и чётное?
# 3. Это число делится на 31 без остатка?
# 4. Если это число больше 100 и оно делится на 17 без остатка или это число больше 150 и равно 13**2 тогда показать что это за число
"""
s = input("number: ")
int(s)
if len(s) == 3:
    print("число трёхзначное")
    if int(s) % 2 == 0 and int(s) > 0:
        print("число чётное")
        print("число положительное")
        if int(s) % 31 == 0:
            print("число делится на 31 без остатка")
            if int(s) > 100 and int(s) % 17 == 0 or int(s) > 150 and int(s) == 13 ** 2:
                print(s)
        else:
            print("число неделится на 31 без остатка")
    else:
        print("число нечётное")
        print("число неположительное")
else:
    print("число нетрёхзначное")
"""

# 9. Сгенерировать 200 чисел от -100 до 100:
# 1. Каждое число которое делиться на 13 без остатка возводить в квадрат если оно чётное
# 2. Каждое 7 число проверять на НЕчестность и выводить на экран если оно нечётное.
# 3. Посчитать сколько чисел подходят под первое условие
# 4. Посчитать сколько чисел подходят под второе условие
'''
num1 = -100
num2 = num1
usl1 = 0
usl2 = 0
while num1 <= 100:
	if num1 % 13 == 0:
		num1 ** 2
		usl1 += 1
		if num1 % 2 == 1:
			usl2 += 1
	num1 += 7
a = str([i for i in range(-100, 100)])
print('Сгенерировать 200 чисел от -100 до 100: ', a)
print('подходят под первое условие: ', usl1)
print('подходят под второе условие: ', usl2)
'''



"""
arr = [21, 123, 54, 6, 798, 654, 97, 651, 8787, 654654, 12132, 5454]
summ = 0
for i in arr:
    summ += i
print(summ)
"""





'''
Наша футбольная команда завершила чемпионат. Результат каждого матча выглядит как "x:y". Результаты всех матчей заносятся в сборник. Например: ["3:1", "2:2", "0:1", ...]
Напишите функцию, которая принимает такой сбор и подсчитывает очки нашей команды в чемпионате. Правила подсчета очков за каждый матч:
если x>y - 3 балла
если x<y - 0 точек
если x=y - 1 балл
'''
'''
resultMatch = ["3:1", "2:2", "0:1", "3:0", "0:0", "0:1", "4:2", "2:1", "1:1", "0:2"]

ball = 0
for i in resultMatch:
	if i[0] > i[2]:
		ball += 3
	elif i[0] < i[2]:
		point = 0
	elif i[0] == i[2]:
		ball += 1

print(ball)
'''







'''
Маша хочет накопить на новый телефон. Телефон стоит
N
рублей. Маша может откладывать
K
рублей в день каждый день, за исключением воскресенья, когда она тратит деньги на поход в кино. Маша начинает копить в понедельник. За сколько дней она накопит нужную сумму?
Входные данные: Вводятся два числа:
N
и
K
.
Входные данные: Выведите искомое количество дней
'''
'''
n = input('Стоимость телефона который Маша хочет: ')
k = input('Маша начинает копить по: ')
day = 0
day += int(n) // int(k)
print(day, 'дней она накопит нужную сумму')
'''




'''
В классе
N
школьников. На уроке физкультуры тренер говорит «на первый-второй рассчитайтесь». Выведите, что скажут ученики.
Входные данные: Вводится одно целое число — количество человек в классе.
Входные данные: Выведите последовательность чисел 1 и 2, в том порядке, как будут говорить школьники.
'''
'''
print('«на первый-второй рассчитайтесь»!!!')
n = int(input('количество человек в классе: '))

for i in range(n):
	if i % 2 == 0:
		print('Первый:', 1)
	else:
		print('Второй:', 2)
'''



'''
Написать скрипт который проходится по ключам и проверяет значения
a) Если значение делиться на 3, то записываем строку “Hi”
b) Если значение делиться на 5, то записываем строку “Bye”
ПРИМЕР:
Дано -> dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
Результат -> a = Bye
b = Hi
'''

'''
dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
print(dict1)
for key, value in dict1.items():
	if value % 3:
		key = 'Bye'
	if value % 5:
		key = 'Hi'
	print(key, value)
'''



'''
Милиардер Илон Маск сбился с счёта он хочет посчитать количество нулей со своего счёта но не может помогите ему
'''
'''
d = [3000000000000]
count = 0
for i in str(d[0]):
	if i == '0':
		count += 1

print(count)
'''



'''
n = int(input())

countZero = 0
while (n % 10 == 0):
    n //= 10
    countZero += 1

print(countZero)
'''




'''
int = 5
float = 5.6
str = 'string'
bool = True

list = [555,3,3,4, str(5)] # изм
tuple = ('sadasddfs,g,dfsg')
set = {'sdklfjldsjfljdslf', 'sdfkjsdhflkjsd',1,1,1,1,1,1,1,} # изм
dict = { 'key' :'valie', 5 : 6, True: [False, True], 3.5:{('r'):[11111]}} # изм
'''