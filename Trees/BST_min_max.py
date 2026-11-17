class BST:
    def __init__(self, key=None):
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


    def min_node(self):
        current = self
        while current.left_child:
            current = current.left_child
        print("Node with the min value is:", current.key)

    def max_node(self):
        current = self
        while current.right_child:
            current = current.right_child
        print("node with the Max value is: ", current.key)






# Example usage
# Create the root of the tree
root = BST(5)

# List of elements to insert into the tree
elements = [1,-4,3,20,100,300]

# Insert elements into the tree
for elem in elements:
    root.insert(elem)


root.min_node()
root.max_node()