import threading
from time import sleep


event = threading.Event()


def run():
    print('1111111111111')
    event.wait()
    print('2222222222222')
    event.clear()
    event.wait()
    print('3333333333333')


if __name__ == '__main__':
    t1 = threading.Thread(target=run)
    t1.start()
    print('等待中...')
    sleep(1)
    event.set()
    sleep(0.1)
    print('等待中...')
    sleep(0.9)
    event.set()
    t1.join()
