# Задание:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.


import time
from threading import Thread

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def subsequence(variable):
    for index in variable:
        print(index, flush=True)
        time.sleep(1)

thread = Thread(target=subsequence, kwargs=dict(variable=numbers))
thread.start()

subsequence(variable=letters)

thread.join()

































