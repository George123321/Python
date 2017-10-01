class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def print(self, node):
        if node is None:
            return
        self.print(node.left)
        print(node.key)
        self.print(node.right)
    def find(self, data):
        p = self.root
        while p is not None and p.key != data:
            if data > p.key:
                p = p.right
            else:
                p = p.left
        return p
    def insert(self, data):
        p = self.find(data)
        if p is not None:
            return
        node = Node(data)
        p = self.root
        if p is None:
            self.root = node
            return
        while True:
            if data > p.key:
                if p.right is None:
                    p.right = node
                    node.parent = p
                    return
                else:
                    p = p.right
            else:
                if p.left is None:
                    p.left = node
                    node.parent = p
                    return
                else:
                    p = p.left