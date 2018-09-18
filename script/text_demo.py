def fei_bo(num):
    pre = 0
    curr = 1
    count = 0
    while count < num:
        result = curr
        count += 1
        curr, pre = curr+pre, curr
        yield result


f = fei_bo(10)
for i in f:
    print(i, end=' , ')

print('-------------------------------------')


class Range:
    def __init__(self, start, end=None, step=1):
        if end is None:
            self.end = start
            self.start = 0
        else:
            self.start = start
            self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            temp = self.start
            self.start = self.start + self.step
            return temp
        else:
            raise StopIteration


My_range = Range(10)
for i in My_range:
    print(i, end=' , ')

print('-------------------------------------')


class Feibo:
    def __init__(self, num):
        self.num = num
        self.pre = 0
        self.curr = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num:
            self.count += 1
            self.curr, self.pre = self.curr + self.pre, self.curr
            return self.curr
        else:
            raise StopIteration


fei_bo = Feibo(5)
for i in fei_bo:
    print(i, end=' , ')
print('-------------------------------------')


class Node:
    def __init__(self, item):
        self.item = item
        self.child1 = None
        self.child2 = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.child1 is None:
                    pop_node.child1 = node
                    return
                elif pop_node.child2 is None:
                    pop_node.child2 = node
                    return
                else:
                    q.append(pop_node.child1)
                    q.append(pop_node.child2)

    def traverse(self):
        if self.root is None:
            return []
        else:
            res = [self.root.item]
            q = [self.root]
            while q:
                pop_node = q.pop(0)
                if pop_node.child1 is not None:
                    res.append(pop_node.child1.item)
                    q.append(pop_node.child1)
                if pop_node.child2 is not None:
                    res.append(pop_node.child2.item)
                    q.append(pop_node.child2)
            return res

    @staticmethod
    def post_order(root):
        if root is None:
            return []
        else:
            res = []
            stack = []
            pop_node = root
            while stack or pop_node:
                while pop_node:
                    stack.append(pop_node)
                    res.append(pop_node.item)
                    pop_node = pop_node.child2
                if stack:
                    pop_node = stack.pop()
                    pop_node = pop_node.child1
            return res[::-1]

    def pre_order(self, root):
        if root is None:
            return []
        else:
            root_item = [root.item]
            left_item = self.pre_order(root.child1)
            right_item = self.pre_order(root.child2)
        return root_item + left_item + right_item


tree = Tree()
for i in range(10):
    tree.add(i)

s = tree.post_order(tree.root)
print(s)
