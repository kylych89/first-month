

# task 1
'''
values = (True, True, "Razakov 32",23, 23.55)

try :
	values = set(values)
except TypeError:
	print('dont use set')

else:
	print('it is ok')
'''
'''
a = []

not_iter = [int, bool, float]

for i in values:
	if type(i) in not_iter:
		a.append(True)
	else:
		a.append(False)

print("можно ли", all(a))
'''



# task 2
'''
d = set()
for i in range(5):
	a = int(input('Введите число: '))
	d.add(a)
print(d)
print(min(d))
'''


# task 3
'''
course = ['all()', 'any()', 'abs()', 'min()', 'eval()', 'reversed()', 'max()', 'slice()', 'round()', 'len()', 'print()', 'input()']
a = input('Введите функцию: ')
if a in course:
	print('есть такая функция!')
	print(a)
else:
	print('такой функции нет!')
'''


# task 4
'''
a = int(input('Введите какую сумму вы хотите? '))

if a < 50000:
	print('Сумма должна быть не меньше 50000 тысячи!')
elif a > 50000:
	b = a * (3.47 / 100)
	print('ваш долг банку: ', round(b))
'''




# task 5
'''
try:
	a = 5
	b = 'hello'
	print(a + b)
except TypeError:
	print('Мы обработали TypeError')
finally:
	print('По любому буду работат!!!')
'''

'''
try:
	a = [1,4,5,9,7,8,0]
	print(a[7])
except IndexError:
	print('Мы ловили IndexError ошибку!')
'''

'''
try:
	a = 4
	print(A)
except NameError:
	print('Мы ловили NameError ошибку!')
'''



# task 6
'''
at = 10
il = 15
wo = 20

try:
	for e in range(-at, at):
		print(wo / e)

	if at > '5':
	        print("at" > 5)

except ZeroDivisionError:
	print('division by zero')

except TypeError:
	print(' > not supported between instances of int and str')
'''




# task 7
'''
lst = []
for i in range(10):
	lst.append(i)

print(lst)

list(reversed(lst))
sls_obj = slice(0, 8)
print(lst[sls_obj])
'''




# task 8
'''
try:
	a = (0)
	b = (1,)
	numbers = []
	while b > a:
		numbers += b
		b += 1
except TypeError:
	print(' > not supported between instances of tuple and int')
'''


# task 9
'''
dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}

try:
	for x in dict_.keys():
		x + 'abc'

except TypeError:
	print('unsupported operand type(s) for +: int and str')
'''
