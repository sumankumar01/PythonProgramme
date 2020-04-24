class kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = kettle("kenwood", 8.99)
print(kenwood.price)
print(kenwood.make)

kenwood.price = 14.12
print(kenwood.price)

haminton = kettle("haminton", 10.99)

print(haminton.price)
print(haminton.make)
