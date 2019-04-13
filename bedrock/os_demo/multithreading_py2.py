import threading

for thread in threading.enumerate():
    print(thread)


def print_thread_info():
    print(threading.active_count())
    print(threading.current_thread())


import time


def add(x, y):
    print("{} + {} = {}".format(x, y, x + y))
    return x + y


def sleepy_add(x, y, sleep_time=5):
    print('{} start sleep'.format(time.time()))
    time.sleep(sleep_time)
    print('{} end sleep'.format(time.time()))
    print("{} + {} = {}".format(x, y, x + y))
    return x + y
