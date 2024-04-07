from random import randint


class Building:
    total = 0
    def __init__(self):
        Building.total += 1
district = []
district_size = randint(20, 100)
while len(district) < district_size:
    new_building = Building()
    district.append(new_building)
print('Всего зданий на улице: ', Building.total)

