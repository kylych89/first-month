'''
#PROBLEM 0
lis = [('str'),(21), (56.3), (True), (False)]
print(lis)
'''

'''
#PROBLEM 1
tupl = ('Hello', 5, True)
print(tupl[0])
print(tupl[1])
print(tupl[2])
'''

'''
#PROBLEM 2
lis = []
lis.append('Python')
lis.append(5)
lis.append(0.15)
lis.append(True)
tupl = ('aibek')
lis.append(tupl)
print(lis)
'''

'''
#PROBLEM 3
lis = ['Bek', 'Marat', 'Almaz', 'Aibek', 'Akyl']
str = ''.join(lis)
print(str)
'''


'''
#PROBLEM 4
lis1 = ['Hello', 8, 7.9]
lis2 = [True, False, 'Python']
lis1.extend(lis2)
print(lis1)
'''


'''
#PROBLEM 5
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
print(names.count('Jack'))
'''


'''
#PROBLEM 6
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
print(names)
names.remove('Oskar')
print(names)
'''


'''
#PROBLEM 7
lis = []
lis.append('Kylych')
lis.append(1989)
lis.append('Python')
print(lis)
'''


'''
#PROBLEM 8
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print('Index of loop is: ', pythonList.index('loop'))
pythonList.remove("loop")
print(pythonList)
'''


'''
#PROBLEM 9
numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
print(len(numbers))
print(numbers[0] * numbers[1])
print(numbers[2] * numbers[3])
print(numbers[4] * numbers[5])
print(numbers[6] * numbers[7])
print(numbers[8] * numbers[9])
print(numbers[10] * numbers[11])
'''


'''
#PROBLEM 10
s = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
nums = []
lets = []

if type(s[0]) == str:
	lets.append(s[0])
elif type(s[0]) == int:
	nums.append(s[0])

if type(s[1]) == str:
        lets.append(s[1])
elif type(s[1]) == int:
        nums.append(s[1])

if type(s[2]) == str:
        lets.append(s[2])
elif type(s[2]) == int:
        nums.append(s[2])

if type(s[3]) == str:
        lets.append(s[3])
elif type(s[3]) == int:
        nums.append(s[3])

if type(s[4]) == str:
        lets.append(s[4])
elif type(s[4]) == int:
        nums.append(s[4])

if type(s[5]) == str:
        lets.append(s[5])
elif type(s[5]) == int:
        nums.append(s[5])

if type(s[6]) == str:
        lets.append(s[6])
elif type(s[6]) == int:
        nums.append(s[6])

if type(s[7]) == str:
        lets.append(s[7])
elif type(s[7]) == int:
        nums.append(s[7])

print(nums)
print(lets)
'''


'''
#PROBLEM 11
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(pythonList[1:4])
'''



'''
# Задача 1
# Есть список:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые больше 5.
 if a.__contains__(5):
     print(a[5:])

 if a[0] > 5:
     print(a[0:])
 elif a[1] > 5:
     print(a[1:])
 elif a[2] > 5:
     print(a[2:])
 elif a[3] > 5:
     print(a[3:])
 elif a[4] > 5:
     print(a[4:])
 elif a[5] > 5:
     print(a[5:])
'''


'''
# Задача 2
# Есть набор чисел
 digits = (113, 118, -5, 1, 135, 137, 0, 142, 144, 17, 154, 0, 155, 2, 159, 172)
# Поделить каждое число из digits на 9 и вывести на экран.
 print(digits[0] / 9)
 print(digits[1] / 9)
 print(digits[2] / 9)
 print(digits[3] / 9)
 print(digits[4] / 9)
 print(digits[5] / 9)
 print(digits[6] / 9)
 print(digits[7] / 9)
 print(digits[8] / 9)
 print(digits[9] / 9)
 print(digits[10] / 9)
 print(digits[11] / 9)
 print(digits[12] / 9)
 print(digits[13] / 9)
 print(digits[14] / 9)
 print(digits[15] / 9)
'''


'''
# Задача 3
 fruits = ('banana', 'stawberry', 'apple', 'orange', 'limon', 'ananas')
# Выведите первый и последний элемент списка.
 print(fruits[0::5])
'''


'''
# Задача 4
"""Здесь замешаны разные типы данных. Если вы уверены что логика написана правильно, но оно всё равно не работает скорее всего вы справились с заданием
Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1."""
 spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
 spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
 if spisok_2[0] == spisok_1[0]:
     print(spisok_2[0])
 elif spisok_2[1] == spisok_1[1]:
     print(spisok_2[1])
 elif spisok_2[2] == spisok_1[2]:
     print(spisok_2[2])
 elif spisok_2[3] == spisok_1[3]:
     print(spisok_2[3])
 elif spisok_2[4] == spisok_1[4]:
     print(spisok_2[4])
 elif spisok_2[5] == spisok_1[5]:
     print(spisok_2[5])
 elif spisok_2[6] == spisok_1[6]:
     print(spisok_2[6])
'''



'''
# Задача 5
# Напишите программу, которая выводит чётные числа из списка длиною 300 объектов
# и останавливается, если встречает число 237.
 lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
        101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
        121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140,
        141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160,
        161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180,
        181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200,
        201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
        221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240,
        241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
        261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280,
        281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300]
 if lis[0] % 2 == 0:
     print(lis[0])
 if lis[1] % 2 == 0:
     print(lis[1])
 if lis[2] % 2 == 0:
     print(lis[2])
 if lis[3] % 2 == 0:
     print(lis[3])
 if lis[4] % 2 == 0:
     print(lis[4])
 if lis[5] % 2 == 0:
     print(lis[5])
 if lis[6] % 2 == 0:
     print(lis[6])
 if lis[7] % 2 == 0:
     print(lis[7])
 if lis[8] % 2 == 0:
     print(lis[8])
 if lis[9] % 2 == 0:
     print(lis[9])
 if lis[10] % 2 == 0:
     print(lis[10])
 if lis[11] % 2 == 0:
     print(lis[11])
 if lis[12] % 2 == 0:
     print(lis[12])
 if lis[13] % 2 == 0:
     print(lis[13])
 if lis[14] % 2 == 0:
     print(lis[14])
 if lis[15] % 2 == 0:
     print(lis[15])

 for el in lis:
     if el % 2 == 0:
         print(el, end=' ')
     if el == 237:
         break
'''

'''
# Задание 6:
#Дан список  целых чисел:
numbers = [0, 2, 4, 7, 1, 8, 0, -3, 7, 0, -2, 4, 0, 0, -1, 7, -43, 0, 8, -3, 6, 9]
#Создайте новый лист и замените отрицательные числа на -1, положительные на число 1, ноль оставить без изменения.
newList = []
if numbers.__contains__(-1):
     newList.extend(numbers)
     newList[14] = 1
     print(numbers)
     print(newList)
'''
