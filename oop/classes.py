# task 1
class Laptop:
    def  __init__(self, cpu, ram, video_card, ssd, mother_board, screen_size) -> None:
        self.cpu = cpu
        self.ram = ram
        self.video_card = video_card
        self.ssd = ssd
        self.mother_board = mother_board
        self.screen_size = screen_size


    def display(self):
        dic = {
            'cpu': self.cpu,
            'ram': self.ram,
            'video_card': self.video_card,
            'ssd': self.ssd,
            'mother_board': self.mother_board,
            'screen_size': self.screen_size
        }
        print(dic)
        # print({'cpu': self.cpu, 'ram': self.ram, 'video_card': self.video_card, 'ssd': self.ssd, 'mother_board': self.mother_board, 'screen_size': self.screen_size})


l = Laptop('intel core i7', '14 GB', 'GEFORCE', 'SSD Teamgroup NVMe MP33 128GB M.2 2280', 'Asus Prime H310M-K','13–15 дюймов 1400 × 1050')
# l.display()
# print(l)



# Data #1:
colors = {
"black": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,255,1],
"hex": "#000"
}
},
"white": {
"category": "value",
"code": {
"rgba": [0,0,0,1],
"hex": "#FFF"
}
},
"red": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,0,0,1],
"hex": "#FF0"
}
},
"blue": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [0,0,255,1],
"hex": "#00F"
}
},
"yellow": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,0,1],
"hex": "#FF0"
}
},
"green": {
"category": "hue",
"type": "secondary",
"code": {
"rgba": [0,255,0,1],
"hex": "#0F0"
}
}
}


# task 2
class TakeDict:
    def __init__(self, dic) -> None:
        self.dic = dic

    def get_keys_tuple(self):
        keys = []
        for i in self.dic.keys():
            keys.append(i)
        
            a = self.dic.get(i)
            for j in a.keys():
                keys.append(j)

                try:
                    d = a.get(j)
                    for s in d.keys():
                        keys.append(s)
                except:
                    pass
        
        print(tuple(keys))
    

    def get_values_tuple(self):
        for i in self.dic.values():
            print(tuple(i))


t = TakeDict(colors)
# t.get_keys_tuple()
print()
# t.get_values_tuple()



