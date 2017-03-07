class bike(object):
    def __init__(self, c, s):
        print "New bike was created"
        self.cost = c
        self.speed = s
        self.miles = 0
    def displayInfo(self):
        print self.cost
        print self.speed
        print self.miles
    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles = self.miles - 5
            return self
        else:
            return self


speedy = bike(100, 15)
red = bike(20, 5)
green = bike(500, 25)

speedy.ride().ride().ride().reverse().displayInfo() 
red.ride().ride().reverse().reverse().displayInfo()
green.reverse().reverse().reverse().displayInfo()
