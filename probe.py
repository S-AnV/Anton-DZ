import time
import queue
import threading

class Table():
    def __init__(self, number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = number
        self.is_busy = False



class Cafe():
    def __init__(self, tables, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customers = queue.Queue() # очередь посетителей
        self.tables = tables # список столов (поступает из вне)
        self.customer_threads = []

    def customer_arrival(self): # моделирует приход посетителя(каждую секунду)
         for customer in range(1, 21):
            print(f'Посетитель номер {customer} прибыл.', flush=True)
            self.serve_customer(customer)
            time.sleep(1)

    def serve_customer(self, customer):
        table_found = False
        for table in self.tables:
            if table.is_busy == False:
                print(f'Посетитель номер {customer} сел за стол {table.number}.', flush=True)
                table.is_busy = True
                customer_task = Customer(customer, table, self.customers, self)
                customer_task.start() # запускаем поток, начинаем обслуживание посетителя
                self.customer_threads.append(customer_task)
                table_found = True
                break

        if not table_found:
            print(f'Посетитель номер {customer} ожидает свободный стол.', flush=True)
            self.customers.put(customer)

                # customer_task.join()

class Customer(threading.Thread): # класс (поток) посетителя. Запускается, если есть свободные столы.
    def __init__(self, id, table, queue, cafe):
        super().__init__()
        self.customers = queue
        self.id = id
        self.table = table
        self.cafe = cafe

    def run(self):
        time.sleep(5)
        print(f'Посетитель номер {self.id} покушал и ушел.', flush=True)
        self.table.is_busy = False
        if not self.customers.empty():
            customer_next = self.customers.get()
            self.cafe.serve_customer(customer_next)


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

for i in cafe.customer_threads:
    i.join()

































