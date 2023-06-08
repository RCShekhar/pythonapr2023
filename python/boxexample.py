class BoxCompany:
    dim = None
    cap = None
    price = None

    def __init__(self, dim, cap, price):
        self.dim = dim
        self.cap = cap
        self.price = price
        self.color = "Gree"
        
    def store_acce(self):
        self.acc = "Books"



me = BoxCompany("20x20", "30L", "$3.5")
me.store_acce()

friend = BoxCompany("40x40", "50L", "$5")
friend.store_acce()

print(me.dim, me.cap, me.price,me.acc)
print(friend.dim, friend.cap, friend.price,friend.acc)




