import random
from time import time
from queue import Queue
from threading import Thread, Lock


q = Queue()


def foo(n):
    x = 0
    for _ in range(n):
        x += random.randint(1, 100)
        # print(f'准备把{x}放进队列q中')
        q.put(x)
    return x


if __name__ == '__main__':
    print('主线程开始...')

    t = Thread(target=foo, args=(1000,))
    t.start()
    t.join()

    print('主线程结束...')


class Time1:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time()
        self.func(*args, **kwargs)
        end = time()
        print(f'耗费时间:{end - start}')


num = 100
lock = Lock()


@Time1
def run(n):
    global num
    for i in range(10000000):
        try:
            # 线程锁的使用相当耗费性能
            lock.acquire()
            num += n
            num -= n
        finally:
            lock.release()


if __name__ == '__main__':
    t1 = Thread(target=run, args=(1,))
    t2 = Thread(target=run, args=(2,))
    t3 = Thread(target=run, args=(3,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(f'num={num}')
