import time
import threading

class Knight (threading.Thread):
    def __init__(self,name, power):
        #threading.Thread.__init__(self)
        super().__init__()
        self.name = name
        self.power = power

    def run (self):
        counter_of_knight = 100
        time_counter=0

        print(f'{self.name}, на нас напали!')
        while counter_of_knight:
            time.sleep(1)
            counter_of_knight -= self.power
            time_counter += 1
            print(f' {self.name} сражается {time_counter} день (дня)..., осталось  {counter_of_knight} воинов.')
        print(f' {self.name} одержал победу спустя {time_counter} дней!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
#second_knight.join()

#print('вне run',first_knight.is_alive())
#print('вне run',second_knight.is_alive())

if not first_knight.is_alive() and second_knight.is_alive:
    print(f'Все битвы закончены!')
