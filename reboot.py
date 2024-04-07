class Building:
    def __init__(self):
        self.numberOfFloors = []
        self.buildingType = []
    def __str__(self):
        return 'Тип здания: ', self.buildingType
    def __int__(self):
        return 'Этажность: ', self.numberOfFloors
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

home = Building()
house = Building()
home.buildingType = 'Многоквартирный'
home.numberOfFloors = 5
house.buildingType = 'Многоквартирный'
house.numberOfFloors = 12

if home == house:
    print('Дом, милый дом!')
else:
    print('Похож, но не наш дом')

house.numberOfFloors = 5

if home == house:
    print('Дом, милый дом!')
else:
    print('Похож, но не наш дом')




