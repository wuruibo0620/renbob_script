import time


def cost_time(func):
    def inner(self):
        startTime = time.time()
        func()
        endTime = time.time()
        print("耗时%d"%(endTime - startTime))
    return inner


class Node(object):
    def __init__(self,item):
        self.item = item
        self.child1 = None
        self.child2 = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            q = [self.root]
            
            while True:
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

    # 层次遍历
    def traverse(self):
        if self.root==None:
            return None

        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.child1 is not None:
                q.append(pop_node.child1)
                res.append(pop_node.child1.item)

            if pop_node.child2 is not None:
                q.append(pop_node.child2)
                res.append(pop_node.child2.item)
        return res

    # 先序遍历
    def preorder(self,root):
        if root == None:
            return []
        result = [root.item]
        leftitem = self.preorder(root.child1)
        rightitem = self.preorder(root.child2)
        return result + leftitem + rightitem

    # 中序遍历
    def inorder(self,root):
        if root == None:
            return []
        result =[root.item]
        leftitem = self.inorder(root.child1)
        rightitem = self.inorder(root.child2)
        return leftitem + result + rightitem

    # 后序遍历
    def postorder(self,root):
        if root == None:
            return []
        result = [root.item]
        leftitem = self.postorder(root.child1)
        rightitem = self.postorder(root.child2)
        return leftitem + rightitem + result

    # 后序遍历
    def postorder1(self):
        if self.root == None:
            return []
        else:
            res = []
            stack = []
            pop_node = self.root
            while pop_node or stack:
                while pop_node:
                    res.append(pop_node.item)
                    stack.append(pop_node)
                    pop_node = pop_node.child2
                if stack:
                    pop_node = stack.pop()
                    pop_node = pop_node.child1

            return res[::-1]


                
if __name__ == '__main__':
    tree = Tree()
    for i in range(1,19):
        tree.add(i)

    print(tree.postorder1())
    # print(tree.preorder(tree.root))
    # print(tree.postorder(tree.root))
    # print(tree.postorderTraversal())


