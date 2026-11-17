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

#root = BST(None)
root = BST(5)

list1 = [20,4,30, 4, 1, 5, 6]
for i in list1:
    root.insert(i)
    
