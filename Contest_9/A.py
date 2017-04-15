class Node:
    def __init__(self, data):
        self.key = data
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def find(self, data):
        p = self.root
        while p is not None and p.key != data:
            if data > p.key:
                p = p.right
            else:
                p = p.left
        return p

    def print(self, node='f'):
        if node == 'f':
            node = self.root
        if node is None:
            return
        self.print(node.left)
        print(node.key, end=' ') # Это не совсем обратный ход рекурсии
        self.print(node.right)

    def add(self, data):
        p = self.find(data)
        if p is not None:
            return
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        p = self.root
        while True:
            if data < p.key:
                if p.left is None:
                    p.left = node
                    node.parent = p
                    break
                else:
                    p = p.left
            else:
                if p.right is None:
                    p.right = node
                    node.parent = p
                    break
                else:
                    p = p.right