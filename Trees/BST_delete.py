#If tree is empty? yes then print a msg if no then find the node (perform search operation) left subtree, right subtree
# and the root, then finally delete the node three cases 1) O child, 2) 1 child, 2) 2 child


class BST:
    def __init__(self, key=None):
        self.key = key
        self.right_child = None
        self.left_child = None

    def insert(self, key):
        if self.key is None:
            self.key = key
        else:
            if key < self.key:
                if self.left_child is None:
                    self.left_child = BST(key)
                else:
                    self.left_child.insert(key)
            else:
                if self.right_child is None:
                    self.right_child = BST(key)
                else:
                    self.right_child.insert(key)

    def delete(self, data):
        if self.key is None:
            print("Tree is empty")
            return self

        if data < self.key:
            if self.left_child:
                self.left_child = self.left_child.delete(data)
            else:
                print("Given node is not present in the tree")
        elif data > self.key:
            if self.right_child:
                self.right_child = self.right_child.delete(data)
            else:
                print("Given node is not present in the tree")
        else:
            if self.left_child is None:
                temp = self.right_child
                self = None
                return temp

            if self.right_child is None:
                temp = self.left_child
                self = None
                return temp

            node = self.right_child
            while node.left_child:
                node = node.left_child
            self.key = node.key
            self.right_child = self.right_child.delete(node.key)

        return self

    def preorder(self):
        if self.key is not None:
            print(self.key, end=" ")
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()

    def inorder(self):
        if self.key is not None:
            if self.left_child:
                self.left_child.inorder()
            print(self.key, end=" ")
            if self.right_child:
                self.right_child.inorder()

    def postorder(self):
        if self.key is not None:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(self.key, end=" ")

# Create the root of the tree
root = BST(5)

# List of elements to insert into the tree
list1 = [20, 4, 30, 1, 10, 40]

# Insert elements into the tree
for i in list1:
    root.insert(i)

# Perform traversals
print("Preorder traversal before deletion:")
root.preorder()
print("\nInorder traversal before deletion:")
root.inorder()
print("\nPostorder traversal before deletion:")
root.postorder()

# Delete a node
root = root.delete(20)
root = root.delete(40)
root = root.delete(30)

# Perform traversals after deletion
print("\n\nPreorder traversal after deletion:")
root.preorder()
print("\nInorder traversal after deletion:")
root.inorder()
print("\nPostorder traversal after deletion:")
root.postorder()
