import threading
from time import sleep

cond = threading.Condition()


def run1():
    for i in range(0, 10, 2):
        if cond.acquire():
            print(i)
            sleep(1)
            cond.wait()
            print('+++++++++++++++++++++++WAIT')
            cond.notify()
            print('+++++++++++++++++++++NOTIFY')


def run2():
    for i in range(1, 10, 2):
        if cond.acquire():
            print(i)
            sleep(1)
            cond.notify()
            print('**************NOTIFY')
            cond.wait()
            print('****************WAIT')


if __name__ == '__main__':
    threading.Thread(target=run1).start()
    threading.Thread(target=run2).start()
