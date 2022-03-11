# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”

from soupsieve import select


class Student:
    def __init__(self, name, lastname, year_of_entrance, department) -> None:
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        return self.name, self.lastname, 'поступил', self.year_of_entrance, 'г.', 'на факультет:', self.department


s = Student('Вася', 'Иванов', 2017, 'Программирование')
# print(s.get_student_info())


# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.
class Airplane:
    def __init__(self) -> None:
        self.make = 'Airbus 300'
        self.model = '777-9 1:200'
        self.year = 2005
        self.max_speed = '800 км/ч'
        self.odometer = 0
        self.is_flying = False

    def __str__(self) -> str:
        return self.make, self.model, self.year, self.max_speed


    def take_off(self):
        t = self.is_flying = True
        return 'взлет is_flying = ', t

    def fly(self, distance):
        self.odometer += distance
        return self.odometer

    def land(self):
        f = self.is_flying = False
        return 'приземление is_flying = ', f


a = Airplane()
# print(a.__str__())
# print(a.take_off())
# print(a.fly(800))
# print(a.land())

# 3)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.
class ContactList(list):
    def search_by_name(self, name):
        all_contacts = ['kiri', 'kylych', 'name', 'askar']
        sovpadenie = []

        for i in all_contacts:
            if i == name:
                sovpadenie.append(i)
        
        return sovpadenie
    
all_contacts = ContactList()
# print(all_contacts.search_by_name('kiri')) 



# 4)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)
# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.

class Soldier():
    def __init__(self) -> None:
        self.name  = 'Ryan'

    def __str__(self) -> str:
        return f'{self.name} is a soldier and can fire! Be careful!'

    

class Guns(Soldier):
    def __init__(self) -> None:
        self.gun = 'K-47'
        self.bullets = 10

                

class Act_of_Shooting(Guns):
    def can_fire(self):
        def reload_bullet(more_bullets):
                print('reload!!!')
                self.bullets += more_bullets
        while self.bullets > 0:
            print('tigi-tigitishh')
            self.bullets -= 1
            
        if self.bullets == 0:
            print('we are out of bullets!')
            reload_bullet(int(input('Патроны кончились! Давай мне патроны! ')))
            print('relaod DONE!')
            print('FIRE!')
        while self.bullets > 0:
                print('tigi-tigitishh')
                self.bullets -= 1
                if self.bullets == 0:
                    print('we are out of bullets!')
                    reload_bullet(int(input('Патроны кончились! Давай мне патроны! ')))
                    if self.bullets == 0:
                        print('We have no bullets! Goodbye')
                    else:
                        print('relaod DONE!')
                        print('FIRE!')
                    
                    
s = Soldier()
print(s)
a = Act_of_Shooting()
a.can_fire()
