from threading import Thread
class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
    def attack

knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()