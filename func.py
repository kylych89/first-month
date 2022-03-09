# Создайте функцию которая которая берёт лист делит его
#  пополам и обе стороны разворачивает в противоположную сторону
# list_1 = ['name', 'age', '1', '19']
# def opposite(lis):
#     lis1 = lis[2:]
#     lis2 = lis[0:2]
#     lis1.reverse()
#     lis2.reverse()
#     print(lis1, lis2)

# opposite(list_1)


# Создайте функцию которая генерирует 10 чисел Фибоначчи: 

# from re import A


# def fibo():
#     return [x[0] for x in [(a[i][0], a.append([a[i][1], a[i][0]+a[i][1]])) for a in ([[1, 1]], ) for i in range(10)]]

# print(fibo())


# def fibonacci(n):
#     i = 0
#     a = 1
#     b = 1
#     fib = [a,b]
#     while i < n:
#         c = a+b
#         a=b
#         b=c 
#         fib.append(c)
#         i+=1
#     print(fib)
# fibonacci(10)


# Создайте функцию сложения, затем функцию вычитания двух чисел...
# Создайте 3-ю функцию которая вызывает первые 2 внутри себя.

# def add(a, b):

#     print(a + b)

# def minus(a, b):
#     print(a - b)

# def all():
#     return add(10, 20), minus(20, 30)

# all()

# Спросите у пользователя имя файла.
# Создайте функцию которая создаёт файл с именем которое передал пользователь.
# Присвойте ИМЯ функции к переменной и вызывайте функцию через переменную
# a = input("Введите имя файла: ")
# def createAFile():
#     f = open(f"/home/kylych/Рабочий стол/python files/{a}", "w")
#     f.write(a)
#     f.close()
#     print("file successfully created!")

# b = createAFile()


# Создайте функцию gen_number() которая генерирует телефонный номер с кодом 0444 _ _ _ _ _ _.
# Номера которые вы можете генерировать могут содержать в себе только числа 145790.
# Пример: 0444150971 0444111777 0444457901
# import random
# def gen_number():
#     suffix = random.randint(9999999, 100000000)
#     return f'0444{suffix}'

# print(gen_number())



# Создайте 4 функции: add(), substract(), multiply(), divide() 
# которые будут принимать по 2 аргумента и возвращать
#  результат: сложения, вычитания, умножения и деления.

# def add(a, b):
#     return a + b

# print(add(10, 15))

# def substract(a, b):
#     return a - b

# print(substract(15, 5))

# def multiply(a, b):
#     return a * b

# print(multiply(5, 6))

# def divide(a, b):
#     return a / b

# print(divide(6, 2))



# Написать Функцию которая принимает предложение как аргумент,
# считает количество букв и возвращает сколько символов он ввёл.
# НЕ ИСПОЛЬЗОВАТЬ функцию len()
# def check_len_str(str1):
#     count_len = 0
#     for i in str1:
#         count_len += 1
#     return count_len
        
# print(check_len_str("kylych"))



# площадь комнаты
# def room_area():
#     sideA = int(input('Длина комнаты: '))
#     sideB = int(input('Ширина комнаты: '))
#     roomArea = sideA * sideB
#     print("Площадь комнаты: ", roomArea)
#     sideSofaA = int(input('Длина дивана: '))
#     sideSofaB = int(input('Ширина дивана: '))
#     sofaArea = sideSofaA * sideSofaB
#     print("Площадь дивана: ", sofaArea)
#     remainder = roomArea - sofaArea
#     print('Площадь комнаты: ', remainder)
    
# room_area()

# def room_area(side1, side2, room_area):
#     room_area = side1 * side2
#     print("Площадь комнаты: ", room_area)
    


