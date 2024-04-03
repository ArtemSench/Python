class Building:
    def __init__(self):
        self.numberOfFloors = 12
        self.buildingType = 'Многоквартирный'
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors
        self.buildingType == other.buildingType

def comparison():
    if Building.__eq__(self=Home, other=House):
        print('Дом, милый дом!')
    else:
        print('Похож, но не наш дом')

Home = Building()
House = Building()
Home.buildingType = 'Многоквартирный'
Home.numberOfFloors = 5
comparison()
House.numberOfFloors = 5
comparison()


