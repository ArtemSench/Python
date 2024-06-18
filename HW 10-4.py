import threading
import queue
import time
import random

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Customer(threading.Thread):
    def __init__(self, customer_id, table, cafe):
        threading.Thread.__init__(self)
        self.customer_id = customer_id
        self.table = table
        self.cafe = cafe

    def run(self):
        print(f"Посетитель номер {self.customer_id} сел за стол {self.table.number}.")
        time.sleep(5)  # время обслуживания (употребление пищи)
        print(f"Посетитель номер {self.customer_id} покушал и ушёл.")
        self.cafe.release_table(self.table)

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.customer_id = 0

    def customer_arrival(self):
        while self.customer_id <= 20:
            time.sleep(random.randint(1, 3))  # моделирование прихода посетителей
            self.customer_id += 1
            print(f"Посетитель номер {self.customer_id} прибыл.")
            self.serve_customer(self.customer_id)

    def serve_customer(self, customer_id):
        free_table = self.find_free_table()
        if free_table:
            free_table.is_busy = True
            customer = Customer(customer_id, free_table, self)
            customer.start()
        else:
            print(f"Посетитель номер {customer_id} ожидает свободный стол.")
            self.queue.put(customer_id)

    def find_free_table(self):
        for table in self.tables:
            if not table.is_busy:
                return table
        return None

    def release_table(self, table):
        table.is_busy = False
        if not self.queue.empty():
            next_customer_id = self.queue.get()
            self.serve_customer(next_customer_id)

if __name__ == "__main__":
    num_tables = 3  # количество столов
    tables = [Table(i) for i in range(1, num_tables + 1)]
    cafe = Cafe(tables)

    # Запуск моделирования прихода посетителей
    threading.Thread(target=cafe.customer_arrival).start()