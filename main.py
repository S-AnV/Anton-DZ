import time
from collections import defaultdict
import queue
import random
import threading

class Table(threading.Thread):
    def __init__(self, number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = number
        self.is_busy = True



class Cafe(threading.Thread):
    def __init__(self, tables, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customers = queue.Queue() # очередь посетителей
        self.tables = tables # список столов (поступает из вне)

    def customer_arrival(self): # моделирует приход посетителя(каждую секунду)
        for customer in range(1, 21):
            print(f'Посетитель номер {customer} прибыл', flush=True)
            self.customer_arrival()
            time.sleep(1)

    def serve_customer(self, customer): # моделирует обслуживание посетителя
# Проверяет наличие свободных столов, в случае наличия стола - начинает обслуживание посетителя (запуск потока),
# в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
        if table1.is_busy:
            self.customers.full(customer)
        else:
            print(f'Посетитель номер {customer} сел за стол {table1.number}.', flush=True)

        # else:


            # if self.customers.put(customer):
            #     print(f'Посетитель номер {customer} сел за стол {table1}.', flush=True)
            # self.customers.full(customer)
            # print(f'Посетитель номер {customer} ожидает свободный стол.', flush=True)




# class Customer: # класс (поток) посетителя. Запускается, если есть свободные столы.



# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)


# Пример работы:
# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

































