import random
from multiprocessing import Process, Queue


dict1 = {'Jack': 21, 'Tom': 22, 'Port': 23, 'Monica': 18}
result = {key: value for value, key in sorted(zip(dict1.values(), dict1.keys()))}
print(result)
print(sorted(dict1.items(), key=lambda x: x[1]))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point((self.x - other.x), (self.y - other.y))
        else:
            raise TypeError('非Point类型')


p1 = Point(4, 2)
p2 = Point(2, 1)
p3 = p1 - p2
print(p3.x, p3.y)


class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def volume(self):
        return self.a * self.b * self.c

    def __eq__(self, other):
        if isinstance(other, Box):
            return self.volume == other.volume
        else:
            raise TypeError('非Box类型')

    def __gt__(self, other):
        if isinstance(other, Box):
            return self.volume > other.volume
        else:
            raise TypeError('非Box类型')

    def __str__(self):
        return f'Box({self.a}, {self.b}, {self.c})'

    def __repr__(self):
        return f'Box({self.a}, {self.b}, {self.c})'


box1 = Box(1, 2, 3)
box2 = Box(2, 1, 3)
box3 = Box(2, 2, 3)
box4 = Box(2, 3, 1)
box5 = Box(2, 5, 1)
boxes = [box1, box2, box3, box4, box5]
sorted(boxes)
print(boxes)

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list1.__setitem__(3, 10)
print(list1)
list1[3] = 100
print(list1)


class Dict(dict):
    # 缺失元素的操作
    def __missing__(self, key):
        raise KeyError('Key not exists')   # 还可以更换成其它的功能


q = Queue()


def foo(n, queue):
    x = 0
    for _ in range(n):
        x += random.randint(1, 100)
        # 准备把x放进队列q中
        queue.put(x)
    return x


def bar(q, n):
    for i in range(n):
        data = q.get()
        print(f'取到了数据{data}')


if __name__ == '__main__':
    p1 = Process(target=foo, args=(1000, q))
    p1.start()

    p2 = Process(target=bar, args=(q, 100))


