class Node(object):  # 定义一个节点对象
    def __init__(self, item):
        self.item = item
        self.child1 = None
        self.child2 = None


class Tree(object):  # 定义一个二叉树对象
    def __init__(self):
        self.root = None

    def add(self, item):  # 定义一个添加节点方法
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            q = [self.root]
            while q:
                pop_node = q.pop(0)
                if pop_node.child1 == None:
                    pop_node.child1 = node
                    return
                elif pop_node.child2 == None:
                    pop_node.child2 = node
                    return
                else:
                    q.append(pop_node.child1)
                    q.append(pop_node.child2)

    def traverse(self):
        if self.root == None:
            return None
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

    def preorder(self,root):    # 定义一个先序遍历方法
        if root == None:
            return []
        else:
            rootItem = [root.item]
            leftItem = self.preorder(root.child1)
            rightItem = self.preorder(root.child2)
        return rootItem + leftItem + rightItem

    def postorder(self,root):
        if root == None:
            return []
        else:
            res = []
            stack = []
            pop_node = root
            while pop_node or stack:
                while pop_node:
                    stack.append(pop_node)
                    res.append(pop_node.item)
                    pop_node = pop_node.child2
                if stack:
                    pop_node = stack.pop()
                    pop_node = pop_node.child1
        return res[::-1]


if __name__ == '__main__':
    tree = Tree()
    for i in range(1,8):
        tree.add(i)

    print(tree.postorder(tree.root))