# task 1
class Laptop:
    def __init__(self, cpu, ram, video_card, ssd, mother_board, screen_size) -> None:
        self.cpu = cpu
        self.ram = ram
        self.video_card = video_card
        self.ssd = ssd
        self.mother_board = mother_board
        self.screen_size = screen_size
        print({'cpu': self.cpu, 'ram': self.ram, 'video_card': self.video_card, 'ssd': self.ssd, 'mother_board': self.mother_board, 'screen_size': self.screen_size})

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


l = Laptop('intel core i7', '14 GB', 'GEFORCE', 'SSD Teamgroup NVMe MP33 128GB M.2 2280', 'Asus Prime H310M-K',
           '13–15 дюймов 1400 × 1050')
# l.display()
print(l)


# Data #1:
colors = {
    "black": {"category": "hue", "type": "primary", "code": {"rgba": [255, 255, 255, 1], "hex": "#000"}},
    "white": {"category": "value", "code": {"rgba": [0, 0, 0, 1], "hex": "#FFF"}},
    "red": {"category": "hue", "type": "primary", "code": {"rgba": [255, 0, 0, 1], "hex": "#FF0"}},
    "blue": {"category": "hue", "type": "primary", "code": {"rgba": [0, 0, 255, 1], "hex": "#00F"}},
    "yellow": {"category": "hue", "type": "primary", "code": {"rgba": [255, 255, 0, 1], "hex": "#FF0"}},
    "green": {"category": "hue", "type": "secondary", "code": {"rgba": [0, 255, 0, 1], "hex": "#0F0"}}
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
        values = []

        for i in self.dic.values():
            values.append(i)

            a = i.values()
            for j in a:
                values.append(j)
                try:
                    b = j.values()
                    for c in b:
                        values.append(c)

                        d = c.vlaues()
                        for e in d:
                            values.append(e)

                            f = e.values()
                            for h in f:
                                values.append(h)
                except:
                    pass

        print(tuple(values))

    def get_keys_list(self):
        keys = []
        for i in self.dic.keys():
            keys.append(i)

            a = self.dic.get(i)
            for j in a.keys():
                keys.append(j)

                try:
                    b = a.get(j)
                    for k in b.keys():
                        keys.append(k)
                except:
                    pass
        print(keys)

    def get_value_list(self):
        values = []
        for i in self.dic.values():
            values.append(i)

            a = i.values()
            for j in a:
                values.append(j)

                try:
                    b = j.values()
                    for k in b:
                        values.append(k)

                        c = k.valuse()
                        for l in c:
                            values.append(l)

                            d = l.values()
                            for m in d:
                                values.append(m)
                except:
                    pass

        print(values)

    def get_keys_set(self):
        sets = []
        for i in self.dic.keys():
            sets.append(i)

            a = self.dic.get(i)
            for j in a.keys():
                sets.append(j)

                try:
                    b = a.get(j)
                    for k in b.keys():
                        sets.append(k)
                except:
                    pass

        print(set(sets))


t = TakeDict(colors)
# t.get_keys_tuple()
# t.get_values_tuple()
# t.get_keys_list()
# t.get_value_list()
# t.get_keys_set()


# task 3
data = {
    "markers": [
        {
            "name": "Rixos The Palm Dubai",
            "position": [25.1212, 55.1535]
        },
        {
            "name": "Shangri-La Hotel",
            "location": [25.2084, 55.2719]
        },
        {
            "name": "Grand Hyatt",
            "location": [25.2285, 55.3273]
        }
    ]
}


class Data:

    def __init__(self, data):
        self.data = data

    
    def get_names_tuple(self):
        # names = [i['name'] for i in self.data.get('markers')]
        
        names = []
        for value in self.data.get('markers'):
            names.append(value['name'])

        return tuple(names)

    def get_location_tuple(self):
        loc = []

        for values in self.data.get('markers'):
            for key, value in values.items():
                if key in ['location','position']:
                    loc.append(value)

        return tuple(loc)
    
    def get_dict_all(self):
        markers = {
            'name':self.get_names_tuple(),
            'location': self.get_location_tuple()
            }
        return markers

    def add_field_id(self):
        for key, val in self.data.items():
            for i in val:
                i['status_id'] = 1
                print(i)
            

d  = Data(data)
# print(d.get_names_tuple())
# print(d.get_location_tuple())
# print(d.get_dict_all())
# d.add_field_id()
