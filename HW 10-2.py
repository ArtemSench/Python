from threading import Thread
import time
from collections import defaultdict
class Knight(Thread):

    def __init__(self, name, skill, warriors, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.warriors = warriors
        self.skill = skill
        self.kill = defaultdict(int)

    def run(self):
        self.kill = defaultdict(int)
        self.dayfight = self.warriors//self.skill
        print(f'{self.name}: на нас напали!')
        for day in range(1, self.dayfight):
            print(f'{self.name}: сражается {day} день(дня)..., осталось {self.warriors - self.skill} воинов.')
            self.warriors = self.warriors - self.skill
        print(f'{self.name}одержал победу спустя {self.dayfight} дней!')
        time.sleep(1)

knight1 = Knight("Sir Lancelot", 10, 100)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20, 100)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
