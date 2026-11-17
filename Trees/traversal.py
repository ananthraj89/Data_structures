class BST:
    def __init__(self, key):
        self.key = key
        self.right_child = None
        self.left_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:   #ignoring duplicate values
            return
        if self.key > data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = BST(data)
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = BST(data) 



    def preorder(self):
        print(self.key, end = " ")
        
        if self.left_child:
            self.left_child.preorder()

        if self.right_child:
            self.right_child.preorder()


    def Inorder(self):
        if self.left_child:
            self.left_child.Inorder()

        print(self.key, end = " ")

        if self.right_child:
            self.right_child.Inorder()

    
    def Postorder(self):
        if self.left_child:
            self.left_child.Postorder()

        if self.right_child:
            self.right_child.Postorder()

        print(self.key, end = " ")


root = BST(5)

list1 = [20,4,30,1, 10,40]
for i in list1:

    root.insert(i)

#perform traversals
print("Preorder Traversal: ")
root.preorder()

print("\nInorder traversal: ")
root.Inorder()

print("\nPostorder Traversal: ")
root.Postorder()