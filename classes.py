class Home:
    def __init__(self):
        self.numberOfHouse = 15
        self.numberOfFlats = 48
my_home = Home()
print('Номер моего дома: ', my_home.numberOfHouse)
print('Номер моей квартиры: ', my_home.numberOfFlats)
my_home.numberOfFloors = 10
while my_home.numberOfFloors > 0:
    print('Текущий этаж равен', my_home.numberOfFloors)
    my_home.numberOfFloors -= 1
    
