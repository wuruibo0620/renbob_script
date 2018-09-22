import threading


local = threading.local()
num = 2


def run(x, n):
    x += n
    x -= n


def func(n):
    local.y = num
    for i in range(10000000):
        run(local.y, n)
    print(local.y)


if __name__ == '__main__':
    t1 = threading.Thread(target=func, args=(3,))
    t2 = threading.Thread(target=func, args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


