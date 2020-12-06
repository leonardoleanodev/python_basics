import os
from multiprocessing import Pool

import random
import time

class PoolRunner(object):
    def __init__(self):
        self.processes = os.cpu_count()-1

    def runner(self, func_list):
        with Pool(self.processes) as p:
            procs = []
            # register the processes
            for func, args in func_list:
                proc = p.apply_async(func, args)
                procs.append(proc)
            
            # run every process in parallel
            for proc in procs:
                proc.get()
        return procs

def f(x):
    for i in range(10):
        a = [i for i in range(10000)]
        a = 23*a
    time.sleep(random.randint(1,3))
    print("result:", sum(a))
    print("process:", x)
    return x

def sleep_print(a):
    time.sleep(random.randint(1,3))
    print(a)

if __name__ == '__main__':
    start = time.time()
    func_list = [
        (sleep_print,('sleep_print',)),
        (print,()),
        (print,()),
        (print,('a')),
        (print,('a')),
        (print,('a','b')),
        (print,('ab',)),
        (sleep_print,('sleep_print',)),
        (sleep_print,('sleep_print1',)),
        (sleep_print,('sleep_print2',)),
        (sleep_print,('sleep_print3',)),
        (sleep_print,('sleep_print4',)),
        (sleep_print,('sleep_print5',)),
    ]

    for i in range(10):
        func_list.append(
            (f,(i,))
        )

    PoolRunner().runner(func_list)

    finish = time.time()
    delta = finish-start
    print(delta)