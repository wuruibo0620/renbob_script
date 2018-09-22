import threading
import random
import queue
from time import sleep


def product(id1, q):
    for _ in range(10):
        num = random.randint(100, 1000)
        q.put(num)
        print(f'第{id1}号生成者,生成了{num}数据!')
        sleep(1)
    q.task_done()


def customer(id2, q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f'第{id2}位消费者,消费了{item}数据!!')
        sleep(1)
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue()
    # 启动生产者
    for i in range(5):
        threading.Thread(target=product, args=(i, q)).start()


    for j in range(3):
        threading.Thread(target=customer, args=(j, q)).start()
