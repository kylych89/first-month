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


