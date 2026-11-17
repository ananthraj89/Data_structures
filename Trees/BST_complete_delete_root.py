#The above program will not execute if the root node is 1 and it wont delete the the node. forthat we need to count the 
#no of nodes n the tree 

#root can be leaf, 1child, 2child



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

    def delete(self, data, curr):
        if self.key is None:
            print("Tree is empty")
            return self

        if data < self.key:
            if self.left_child:
                self.left_child = self.left_child.delete(data, curr)
            else:
                print("Given node is not present in the tree")
        elif data > self.key:
            if self.right_child:
                self.right_child = self.right_child.delete(data, curr)
            else:
                print("Given node is not present in the tree")
        else:
            if self.left_child is None:
                temp = self.right_child
                #deleting root node, left child is None
                if data == curr:
                    self.key = temp.key                           
                    self.left_child = temp.left_child
                    self.right_child = temp.right_child
                    temp = None
                    return
                self = None
                return temp

            if self.right_child is None:
                temp = self.left_child
                #deleting root node if right child is None
                if data == curr:
                    self.key = temp.key
                    self.left_child = temp.left_child
                    self.right_child = temp.right_child
                    temp = None
                    return
                self = None
                return temp

            node = self.right_child
            while node.left_child:
                node = node.left_child
            self.key = node.key
            self.right_child = self.right_child.delete(node.key, curr)

        return self

#counting the nodes to delete the root node
def count(node):
    if node is None:
        return 0
    return 1+ count(node.left_child) + count(node.right_child)



# Example usage
# Create the root of the tree
root = BST(5)

# List of elements to insert into the tree
elements = [1,-4,3,20,100,300]

# Insert elements into the tree
for elem in elements:
    root.insert(elem)

# Print the tree before deletion
print("Tree before deletion:")
print(root.key)  # Root node
print(root.left_child.key if root.left_child else None)  # Left child of root
print(root.right_child.key if root.right_child else None)  # Right child of root

# If the root node is a leaf node, we should call the root node as well and in the function add curr
print("\nAttempting to delete the root node...")
if count(root) > 1:                    
    root.delete(5, root.key)
else:
    print("Can't perform deletion operation")

# Print the tree after deletion
print("\nTree after deletion:")
print(root.key)  # Root node
print(root.left_child.key if root.left_child else None)  # Left child of root
print(root.right_child.key if root.right_child else None)  # Right child of root

