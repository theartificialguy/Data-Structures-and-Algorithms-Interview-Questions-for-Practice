class node:
    def __init__(self,data=None):
        self.left = None
        self.value = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value,self.root)
    
    def _insert(self,value,curr):
        if value < curr.value:
            if curr.left == None:
                curr.left = node(value)
            else:
                self._insert(value,curr.left)
        elif value > curr.value:
            if curr.right == None:
                curr.right = node(value)
            else:
                self._insert(value,curr.right)
        else:
            print"value already in tree!"
        
    def display(self):
        if self.root!=None:
            self._display(self.root)
        
    def _display(self,curr):
        if curr!=None:
            self._display(curr.left)
            print(str(curr.value))
            self._display(curr.right)

    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0
    
    def _height(self,curr_node,curr_height):
        if curr_node == None:
            return curr_height
        left_height = self._height(curr_node.left,curr_height+1)
        right_height = self._height(curr_node.right,curr_height+1)
        return max(left_height,right_height)

def driver_code(tree,num=10,max_int=100):
    from random import randint
    for _ in range(num):
        element = randint(0,max_int)
        tree.insert(element)
    return tree

tree = BST()
driver_code(tree)
tree.display()
print"height of the tree: "
print(tree.height())