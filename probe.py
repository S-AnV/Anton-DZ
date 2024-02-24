# Задание:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.

# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions)
# при модификации общего ресурса.

# Примечание:
# Используйте класс Lock из модуля threading для блокировки доступа к общему ресурсу.
# Ожидается создание двух потоков, один для пополнения счета, другой для снятия денег.
# Используйте with (lock object): в начале каждого метода, чтобы использовать блокировку

import threading

class BankAccount():

    def __init__(self):
        self.balance = 1000
        self.balance_lock = threading.Lock()

    def deposit(self, num):
        with self.balance_lock:
            self.balance += num
        print(f'Deposited {num}, new balance is {self.balance}')

    def withdraw(self, num):
        with self.balance_lock:
            self.balance -= num
        print(f'Withdrew {num}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)

account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()































