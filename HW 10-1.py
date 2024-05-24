import time
from threading import Thread
def count(lst):
    for n in range(len(lst)):
        print(lst[n])
        time.sleep(1)

lst1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
lst2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

thread = Thread(target=count, kwargs=dict(lst=lst1))
thread.start()

count(lst=lst2)

thread.join()