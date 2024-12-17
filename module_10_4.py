# Задача "Потоки гостей в кафе":
import queue
import time
import threading
from threading import current_thread
from time import sleep
import random
from queue import Queue

global free_tables

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest (threading.Thread):
    def __init__(self, name):
        super().__init__()
        #threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f'поток запущен {self.name} ')
        time_delay = random.randint(3, 10)
        sleep(time_delay)
        #print(f'текущий поток Гостя {threading.current_thread()}')
        #print(f'текущий поток Гостя {threading.current_thread().is_alive}')
        #print(f'текущий поток Гостя в RUN = {threading.current_thread().name} жив или нет:  {self.is_alive()}')
        #print(f'перечень запущенных потоков внутри Run {threading.enumerate()}')
        #print(f' количестов живых потоков внутри Run  {threading.active_count()}')

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival (self,*guests):
        global free_tables
        free_tables = len(tables)

        for guest in guests:
            if free_tables > 0:
                for i in range(len(tables)): # ищем/проверяем есть ли в кафе пустой стол
                    if self.tables[i].guest is None: # стол не занят
                        self.tables[i].guest = guest # посадили Гостя за свободный по порядку стол
                        print (f'{self.tables[i].guest.name} сел(-а) за стол номер {self.tables[i].number}' )
                        #print(f'текущий поток в Arrival {threading.current_thread()}')
                        guest.start()
                        free_tables -= 1
                        break

            elif free_tables == 0: # если свободных столов нет, то ставим гостя в очередь
                cafe.queue.put(guest)
                print(f'{guest.name} в очереди') #=.put(guest)

        return (print('все гости прибыли'))

    def discuss_guests (self):
        #free_tables=0
        #while not self.queue.empty() or free_tables<len(tables):

        while not self.queue.empty():
            for i in range(len(tables)):

                if self.tables[i].guest is not None and not self.tables[i].guest.is_alive():
                    print(f'Гость {self.tables[i].guest.name} покушал (а) и ушел (ушла)')
                    print(f'Стол номер {self.tables[i].number} свободен')
                    self.tables[i].guest = None #освободили текущий стол

                if not self.queue.empty() and self.tables[i].guest is None:
                    self.tables[i].guest = cafe.queue.get() # посадили Гостя из очереди за освободившийся стол
                    print(f'{self.tables[i].guest.name} вышел(-ла) из очереди '
                          f'и сел(-а) за стол номер {self.tables[i].number}>'
                          f'')
                    self.tables[i].guest.start() #запустили новый поток Гостя

        # если очередь пустая, то завершаем обслуживание занятых столов
        else:
            for i in range(len(tables)):
                if self.tables[i].guest is not None and not self.tables[i].guest.is_alive():
                    #print(f'поток гостя {self.tables[i].guest.is_alive()}')
                    print(f'Гость {self.tables[i].guest.name} покушал (а) и ушел (ушла)')
                    print(f'Стол номер {self.tables[i].number} свободен')
                    self.tables[i].guest = None  # освободили текущий стол



# Создание столов
tables = [Table (number) for number in range(1, 6)]
#print(f'Создание столов {tables}')

# Имена гостей
guests_names = [
            'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
            'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]


# Создание гостей
guests = [Guest(name) for name in guests_names]
print (f'Создание гостей {guests}')

# Заполнение кафе столами
cafe = Cafe(*tables)
print (f'создали Cafe {Cafe}')

# Приём гостей
cafe.guest_arrival(*guests)
#print(f'перечень запущенных потоков {threading.enumerate()}')
#print(f'количестов потоков {threading.active_count()}')
#print(guests[0].is_alive)''

# Обслуживание гостей
cafe.discuss_guests()
