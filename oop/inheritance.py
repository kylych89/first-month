# task 1
class Factory:

    def engine(self):
        return 'Двигатель создан'

    def bridge(self):
        return 'Ходовая часть создана'

class Toyota(Factory):
    def wheels(self):
        return 'Колёса готовы'

    def windows(self):
        return 'Стёкла готовы'

t = Toyota()



# task 2
class Zoo:
    def __init__(self) -> None:
        self.animal_1 = 'Тигр'
        self.animal_2 = 'Бегемот'
        self.animal_3 = 'Жираф'
        lis = [self.animal_2, self.animal_3]
        self.animal_4 = lis

z = Zoo()
# print(z.animal_1)
# print(z.animal_2)
# print(z.animal_3)
# z.animal_1 = 'Лев'
# print()
# print(z.animal_1)
# print()
# print(z.animal_4)
# z.animal_3 = 'Змея'
# print()
# print(z.animal_3)


# task 3
class Furniture:
    def __init__(self, name, bed, cupboard, table):
        self.name = name
        self.bed = bed
        self.cupboard = cupboard
        self.table = table


class Home(Furniture):
    def __init__(self, name, square, bed, cupboard, table):
        super().__init__(name, bed, cupboard, table)
        self.name = name
        self.square = square

    def count(self):
        count = self.square - self.bed - self.cupboard - self.table
        print("Тип дома:", self.name)
        print("общая площадь:", self.square)
        print("оставшаяся площадь дома:", count)
        print("Кровать:", self.bed)
        print("Шкаф::", self.cupboard)
        print("Стол::", self.table)


h = Home('my home', 20, 4, 2, 1.5)
# h.count()


# task 4
class Car:
    def __init__(self, make, model, year, odometer=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel

    def drive(self, km):
        fuel = km / 10
        if self.fuel >= fuel:
            self.__add_distance(km)
            self.__subtract_fuel(fuel)
            print("lets drive!")
        else:
            print('Need more fuel, please, fill more!')

    def __add_distance(self, km):
        self.odometer += km

    def __subtract_fuel(self, fuel):
        self.fuel -= fuel


c = Car("Japan", 'Toyota', 2003)
# c.drive(200)
