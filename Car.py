#definte class & set attributes (price, speed, fuel, mileaage)
class Car(object):
    
    #set function display_all() that returns all the information about the car as a string.
    def display_all(self):
        print ('Price: $' + str(self.price))
        print ('Speed: ' + str(self.speed) + 'mph')
        print ('Fuel: ' + str(self.fuel))
        print ('Mileage: ' + str(self.mileage) + 'mpg')
        print ('Tax: ' + str(self.tax * 100) + '%')
        print (' ')

        return (str(self.price) + str(self.speed) + str(self.fuel) + str(self.mileage) + str(self.tax) )

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        
        #if price > 10k set tax = 15%, else 12%
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        #within init call display_all() to display all car info once defined
        self.display_all()

car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
car6 = Car(20000000, 35, 'Empty', 15)