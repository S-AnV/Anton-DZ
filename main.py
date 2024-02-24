# Задание:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.

# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions)
# при модификации общего ресурса.

# Примечание:
# Используйте класс Lock из модуля threading для блокировки доступа к общему ресурсу.
# Ожидается создание двух потоков, один для пополнения счета, другой для снятия денег.
# Используйте with (lock object): в начале каждого метода, чтобы использовать блокировку

import random
from collections import defaultdict
import threading


class BankAccount(threading.Thread):

    def __init__(self, lock, deposit, withdraw, account=1000, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deposit = deposit
        self.withdraw = withdraw
        self.account = account
        self.account_lock = lock

    def deposit_task(self, account, amount):  # счет, количество
        for _ in range(5):
            account.deposit(amount)
            with self.account_lock:
                self.account += amount
            print(f'Deposited {amount}, new balance is {self.account}')

    def withdraw_task(self, account, amount):
        for _ in range(5):
            account.withdraw(amount)
            with self.account_lock:
                self.account -= amount

            print(f'Withdrew {amount}, new balance is {self.account}')
            account = BankAccount()


account = BankAccount
# account.deposit_task()
# deposit_task = BankAccount.deposit_task
# withdraw_task = BankAccount.withdraw_task

# deposit_thread = BankAccount.deposit_task(1000, 100)
#     account = 1000
lock = threading.Lock()
deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

# Вывод в консоль:
# Deposited 100, new balance is 1100
# Deposited 100, new balance is 1200
# Deposited 100, new balance is 1300
# Deposited 100, new balance is 1400
# Deposited 100, new balance is 1500
# Withdrew 150, new balance is 1350
# Withdrew 150, new balance is 1200
# Withdrew 150, new balance is 1050
# Withdrew 150, new balance is 900
# Withdrew 150, new balance is 750




























