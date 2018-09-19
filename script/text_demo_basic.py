import random
import time


class Feibo:
    def __init__(self, num):
        self.pre = 0
        self.curr = 1
        self.num = num
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num:
            self.count += 1
            temp = self.curr
            self.curr = self.curr + self.pre
            self.pre = temp
            return temp
        else:
            raise StopIteration


my_fei_bo = Feibo(5)
for i in my_fei_bo:
    print(i)


s = 'abcd'
list1 = {val: i*4 for val, i in zip(s, [[1], [2], [3], [4]])}
list2 = {val: [index+1]*4 for index, val in enumerate(s)}
print(list2)

dick = enumerate(s)
print()


class Random1:
    def __init__(self):
        self.times = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.times < 30:
            self.times += 1
            temp = random.randint(1, 51)
            return temp
        raise StopIteration


my_random = Random1()
for i in my_random:
    print(i, end=", ")


print('-----------------------------------')
print('')


def time_cost(func):
    def wrap(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('耗时: %f' % (end_time - start_time))
    return wrap


@time_cost
def my_sum(num):
    result = 0
    for item in range(num):
        result += item
    return result


@time_cost
def my_sleep():
    print('呼呼大睡!')
    time.sleep(2)


my_sleep()

print("--------------------------------")


def control_time(times):
    def wrap(fun):
        def inner(*args, **kwargs):
            time.sleep(times)
            fun(*args, **kwargs)
        return inner
    return wrap


@control_time(3)
def play(name):
    print('开始玩%s' % name)
    print('时间到了不玩了!')


play('lol')


print("--------------------------------------")


class Wraper(object):
    def __call__(self, *args, **kwargs):
        print('++++++++++++++++++++')


@Wraper
def hello():
    print("Hello World!")


hello()
