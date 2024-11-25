# Задача "Банковские операции":

import time
import threading
import random
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        self.lock.acquire()

        for i in range(100):
            operation = random.randint(50, 500)

            if self.balance > 500 and self.lock.locked():
                self.balance += operation
                print(f'Пополнение: {operation}. Баланс: {self.balance}')
                self.lock.release()

            else:
                self.balance += operation
                print(f'Пополнение: {operation}. Баланс: {self.balance}')

            sleep(0.01)


    def take(self):

        for i in range(100):
            operation = random.randint(50, 500)
            print(f'Запрос на {operation}')

            if operation <= self.balance:
                self.balance -= operation
                print(f'Снятие: {operation}. Баланс: {self.balance}')

            elif operation > self.balance:
                print(f'Запрос отклонён, недостаточно средств:')
                self.lock.acquire()



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
