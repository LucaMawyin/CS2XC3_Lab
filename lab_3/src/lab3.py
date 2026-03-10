class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        """
        example from: https://www.geeksforgeeks.org/dsa/c-program-red-black-tree-insertion/
        x: Current Node
        T1, T2, T3, T4, and T5 are subtrees

               g
              / \
            p     u
           / \   / \
          x  T3 T4 T5
         / \
        T1 T2

        Right Rotate on g:

             p
            / \
          x     g
         / \   / \
        T1 T2 T3  u
                 / \
                T4 T5
        """
        # setting p's right child to g's left child
        temp = self.left # temp := p
        self.left = temp.right 
        if self.left: # adjusting parental connection
            self.left.parent = self 

        # fixing p's parental connections (to match g's prior)  
        temp.parent = self.parent 
        if self.parent:
            if self == self.parent.left: 
                self.parent.left = temp
            else:
                self.parent.right = temp

        # g becoming p's right child
        temp.right = self
        self.parent = temp

    def rotate_left(self):
        """ 
        example from: https://www.geeksforgeeks.org/dsa/c-program-red-black-tree-insertion/
        x: Current Node
        T1, T2, T3, T4, and T5 are subtrees

                g
               / \
             u     p
            / \   / \
           T1 T2 T3  x
                    / \
                   T4 T5

        Left Rotate on g:
                p
              /   \
             g     x
            / \   / \
           u  T3 T4 T5
          / \
         T1 T2
        """
        # setting p's left child to g's left right
        temp = self.right # temp := p
        self.right = temp.left
        if self.right: # adjusting parental connection
            self.right.parent = self
        
        # fixing p's parental connections (to match g's prior)  
        temp.parent = self.parent 
        if self.parent:
            if self == self.parent.left: 
                self.parent.left = temp
            else:
                self.parent.right = temp

        # g becoming p's left child
        temp.left = self
        self.parent = temp


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        assert node
        assert node.is_red()
        
        while node.parent != None and node.parent.is_red(): 
            grandparent = node.parent.parent 
            uncle = node.get_uncle()
            assert grandparent
            
            if uncle and uncle.is_red():
                grandparent.make_red()
                node.parent.make_black()
                uncle.make_black()
                node = grandparent
            elif uncle == grandparent.right:
                if node.parent.right == node:
                    node.parent.rotate_left()
                grandparent.rotate_right()
                grandparent.colour, grandparent.parent.colour = grandparent.parent.colour, grandparent.colour
            else:
                if node.parent.left == node:
                    node.parent.rotate_right()
                grandparent.rotate_left()
                grandparent.colour, grandparent.parent.colour = grandparent.parent.colour, grandparent.colour
            
            while self.root.parent:
                self.root = self.root.parent

                
        self.root.make_black()
                    
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"

