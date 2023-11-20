class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data=None):
        if data:
            self.root = Node(data)
        else:
            self.root = None

    def insert(self, data):
        if self.root:
            if data < self.root.data:
                if self.root.left:
                    self.root.left.insert(data)
                else:
                    self.root.left = BinaryTree(data)
            else:
                if self.root.right:
                    self.root.right.insert(data)
                else:
                    self.root.right = BinaryTree(data)
        else:
            self.root = Node(data)

    def inorder(self):
        if self.root is None:
            return
        if self.root.left is not None:
            self.root.left.inorder()
        print(self.root.data)
        if self.root.right is not None:
            self.root.right.inorder()

    def preorder(self):
        if self.root is None:
            return
        print(self.root.data)
        if self.root.left is not None:
            self.root.left.preorder()
        if self.root.right is not None:
            self.root.right.preorder()

    def postorder(self):
        if self.root is None:
            return
        if self.root.left is not None:
            self.root.left.postorder()
        if self.root.right is not None:
            self.root.right.postorder()
        print(self.root.data)

    def delete(self, data):
        if self.root is None:
            return None
        if data < self.root.data:
            if self.root.left is not None:
                self.root.left = self.root.left.delete(data)
        elif data > self.root.data:
            if self.root.right is not None:
                self.root.right = self.root.right.delete(data)
        else:
            if self.root.left is None:
                temp = self.root.right
                self.root = None
                return temp
            elif self.root.right is None:
                temp = self.root.left
                self.root = None
                return temp
            temp = self.root.right
            while temp.root.left is not None:
                temp = temp.root.left
            self.root.data = temp.root.data
            self.root.right = self.root.right.delete(temp.root.data)
        return self


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    tree.delete(50)

    print("Inorder traversal of the original tree:")
    tree.inorder()

    print("\nPreorder traversal of the original tree:")
    tree.preorder()

    print("\nPostorder traversal of the original tree:")
    tree.postorder()
