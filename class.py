class Car:
  def __init__(self):
    self.price = 1000000
  def horse_powers(self):
    self.horse_powers = 100
    return 'У машины {} лошадиных сил'.format(self.horse_powers)

class Nissan (Car):
  def __init__(self):
    self.price = 2000000
  def horse_powers(self):
    self.horse_powers = 200
    return 'У Nissan {} лошадиных сил'.format(self.horse_powers)

class Kia (Car):
    def __init__(self):
        self.price = 1500000
    def horse_powers(self):
        self.horse_powers = 150
        return 'У Kia {} лошадиных сил'.format(self.horse_powers)


my_car = Car()
print (f'Стоимость моей машины {my_car.price}. {my_car.horse_powers()}')

boss_car = Nissan ()
print (f'Стоимость машины шефа {boss_car.price}. {boss_car.horse_powers()}')

friend_car = Kia ()
print (f'Стоимость машины друга {friend_car.price}. {friend_car.horse_powers()}')