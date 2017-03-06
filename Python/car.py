class car(object):
    def __init__(self,p, s, f, m):
        print "New Car has been Created"
        self.price = p
        self.speed = s
        self.fuel = f
        self.mileage = m
        if p > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def displayAll(self):
        print "price = ", str(self.price)
        print "speed = " + str(self.speed)
        print "fuel = " + self.fuel
        print "mileage = " + str(self.mileage)
        print "tax = " + str(self.tax)

red = car(20000, 70, "Full", 15000)
red.displayAll()
green = car(5000, 50, "Empty",150000)
green.displayAll()
black = car(70000, 225, "Full", 15)
black.displayAll()
gray = car(35000, 85, "Kind of Full", 25000)
gray.displayAll()
orange = car(15000, 100, "Empty", 16000)
orange.displayAll()
pink = car(12000000, 100000, "Full", 0)
pink.displayAll()
