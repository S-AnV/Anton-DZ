import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.enemies = 100
        self.day = 0

    def run(self):
        for skill in range(self.skill):
            self.day += 1
            self.enemies -= self.skill
            print(f'{self.name}, сражается {self.day} день(дня)..., осталось {self.enemies} воинов', flush=True)
            time.sleep(1)
            if self.enemies == 0:
                print(f'{self.name} одержал победу спустя {self.day} дней!', flush=True)
                return self.run


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения

print('Sir Lancelot, на нас напали')
print('Sir Galahad, на нас напали')

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print('Все битвы закончились!')