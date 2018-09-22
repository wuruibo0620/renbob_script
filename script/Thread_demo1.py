import threading
from time import sleep


sem = threading.Semaphore(3)  # 第一个位置参数确定最多同时运行几个线程
bar = threading.Barrier(4)


def run(num1):
    sem.acquire()
    print(f'{threading.current_thread().name}:{num1}')
    sleep(2)
    sem.release()


def pao(num1):
    # print(f'{threading.current_thread().name}:{num1}')
    sleep(1.4)
    bar.wait()
    print(f'{threading.current_thread().name}:{num1}')


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=pao, args=(i,)).start()
