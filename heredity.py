class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        self.horse_powers = 100
        return f'У машины ценой {self.price} - {self.horse_powers} лошадиных сил'

class Nissan (Vehicle, Car):

    def __init__(self):
        super().__init__(self)
        self.vehicle_type = 'Седан'

    def __init__(self):
        super(Car).__init__()
        self.price = 2000000

    def horse_powers(self):
        super().horse_powers(self)
        self.horse_powers = 200
        self.vehicle_type = 'седан'
        self.price = 2000000
        return f'У Nissan, с кузовом {self.vehicle_type} и ценой {self.price} - {self.horse_powers} лошадиных сил'

sports_car = Nissan()
car = Car()
print(car.price)
print(sports_car.price)
print(sports_car.horse_powers())
print(sports_car.vehicle_type)


