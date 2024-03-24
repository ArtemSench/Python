class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Мой этаж: ', floors, '-й')
my_home = House()
my_home.setNewNumberOfFloors(7)