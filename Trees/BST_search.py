

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


    def search(self, data):
        if self.key == data:
            print("Node is found")
            return
        
        if data < self.key:
            if self.left_child:
                self.left_child.search(data)
            else:
                print("Node is not found in the Binary Tree")
        else:
            if self.right_child:
                self.right_child.search(data)
            else:
                print("Node is not found")


root = BST(5)
list1 = [20, 4, 30, 4, 1, 5, 6]

for i in list1:
   root.insert(i)

#perform search
root.search(20)
root.search(30)
root.search(500)

