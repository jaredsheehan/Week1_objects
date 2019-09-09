class Bike:

    def __init__(self, color, price):

        self.color = color
        self.price = price

    def getX(self):
        return self.color

    def getY(self):
        return self.price

    def __str__(self):
        return "x = {}, y = {}".format(self.color, self.price)

testOne = Bike("blue", 89.99)
testTwo = Bike("purple",25.0)
print(testOne)
print(testTwo)

''' NEXT PROBLEM'''

class AppleBasket:

    def __init__(self, apple_color, apple_quantity):

        self.apple_color = apple_color
        self.apple_quantity = apple_quantity
    
    def getX(self):
        return self.apple_color

    def getY(self):
        return self.apple_quantity
    
    def increase(self):
        return self.apple_quantity + 1
    
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)
    
    
p = AppleBasket("blue", 9)
print(p)
p1 = p.increase()
print(p1)

''' NEXT PROBLEM '''

class BankAccount:

    def __init__(self, name, amt):

        self.name = name
        self.amt = amt
    
    def getX(self):
        return self.name

    def getY(self):
        return self.amt
    
    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt)
    
    
t1 = BankAccount("Bob", 100)
print(t1)
