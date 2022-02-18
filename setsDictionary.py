'''
#SETS
#PROBLEM 0
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
print(dates_of_birth.discard(7))
'''

'''
#PROBLEM 1
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1.intersection(farm_2)
print(farm_1)
'''


'''
#PROBLEM 2
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2.difference(farm_1)
print(farm_2)
'''


'''
#PROBLEM 3
s = {1, 2, 'hello', True, 2.5}
lis = (4, 5)
s.add(lis)
s.pop()
print(s)
'''


'''
#DICTIONARIES
#PROBLEM 000
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'besh_barmak': 130})
print(menu)
menu.update({'lagman': 135})
print(menu)
menu.pop('borsh')
print(menu)
'''


'''
#PROBLEM 10
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'drinks': ['Coca-Cola', 'Sprite', 'Fanta']})
print(menu)
'''


'''
#PROBLEM 020
set1 = {'add()', 'update()', 'intersection()', 'remove()', 'difference()', 'intersection_update()', 'clear()', 'discard()', 'pop()'}
set2 = {'clear()', 'get()', 'keys()', 'values()', 'items()', 'update()'}
s = set1.intersection(set2)
print(s)
'''


'''
#PROBLEM 31
inp1 = input('enter your name and your password: ')
inp2 = input('enter your name and your password: ')
inp3 = input('enter your name and your password: ')
inp4 = input('enter your name and your password: ')
dic = {}
dic.update({inp1: inp2, inp3: inp4})
print(dic)
'''



'''
#PROBLEM 27
dic = {'kylych': 'programmer', 'aktan': 'driver', 'aibek': 'cooker', 'marat': 'seller', 'asylbek': 'mehanic'}
print(dic)
for i in dic:
	print(f'Здравствуйте: {i}   Прекрасная профессия: {dic.get(i)}')
'''


'''
#PROBLEM 22
inp1 = input('Enter ten number: ')
inp = input('Enter ten number: ')
inp = input('Enter ten number: ')
inp = input('Enter ten number: ')
inp = input('Enter ten number: ')
inp = input('Enter ten number: ')
inp = input('Enter ten number: ')
inp = input('Enter ten number: ')
inp = input('Enter ten number: ')
inp = input('Enter ten number: ')
set1 = {}
set1.add(inp)
print(set1)
'''


'''
# PROBLEM 22
enterSet1 = int(input("Enter number 1: "))
enterSet2 = int(input("Enter number 2: "))
enterSet3 = int(input("Enter number 3: "))
enterSet4 = int(input("Enter number 4: "))
enterSet5 = int(input("Enter number 5: "))
enterSet6 = int(input("Enter number 6: "))
enterSet7 = int(input("Enter number 7: "))
enterSet8 = int(input("Enter number 8: "))
enterSet9 = int(input("Enter number 9: "))
enterSet10 = int(input("Enter number 10: "))

n = set()
n.add(enterSet1)
n.add(enterSet2)
n.add(enterSet3)
n.add(enterSet4)
n.add(enterSet5)
n.add(enterSet6)
n.add(enterSet7)
n.add(enterSet8)
n.add(enterSet9)
n.add(enterSet10)
print(n)
t = tuple(n)
print(t)

# PROBLEM 11
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay',
                            'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
print(south_american_countries)
s = set(south_american_countries)
print(s)

# PROBLEM 101
suitcase = ["shirt", 'waistcoat', 'sweatshirt', 'jumper', 'jacket']
print(suitcase)
suitcase.pop()
print(suitcase)

# PROBLEM 001
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print("First set: ", farm_1)
print("Second set: ", farm_2)
s = set()
s.update(farm_1, farm_2)
print("Third set: ", s)

# PROBLEM 100
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
new_farm = farm_2.copy()
new_farm.update(farm_1)
print(new_farm)
'''
