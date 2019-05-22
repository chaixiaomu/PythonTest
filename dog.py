

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()


    def update_odometer(self,mileage):

        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading +=miles


    def read_odometer(self):
        print("this car has " + str(self.odometer_reading)+" miles on it")


class 



my_new_car = Car("audi","a8",2016)



print(my_new_car.get_descriptive_name())
        
my_new_car.update_odometer(23500)
my_new_car.read_odometer()


my_new_car.increment_odometer(100)

my_new_car.read_odometer()
