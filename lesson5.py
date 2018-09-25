import sys

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, rootNode):
        self.root = rootNode

    def search(self, find_val):
        if(self.root.value == find_val):
            return True
        elif(self.root.left != None):
            lSubTree = BinaryTree(self.root.left)
            if(lSubTree.search(find_val)):
                return True
        elif(self.root.right != None):
            rSubTree = BinaryTree(self.root.right)
            if(rSubTree.search(find_val)):
                return True
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        val = self.root.value
        sys.stdout.write('%s' %val)
        if(self.root.left != None):
            #print('going left')
            sys.stdout.write('-')
            lSubTree = BinaryTree(self.root.left)
            lSubTree.print_tree()
        if(self.root.right != None):
            #print('going right')
            sys.stdout.write('-')
            rSubTree = BinaryTree(self.root.right)
            rSubTree.print_tree()
        return ""

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        return

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(Node(1))
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
#print (tree.search(4))
# Should be False
#print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
#print (tree.print_tree())


#BST Problem Set

#####################

class BST(object):
    def __init__(self, rootNode):
        self.root = rootNode
    def insert(self, new_val):
        if(new_val < self.root.value):
            if(self.root.left == None):
                self.root.left = Node(new_val)
            else:
                leftSubTree = BST(self.root.left)
                leftSubTree.insert(new_val)
        elif(self.root.right == None):
            self.root.right = Node(new_val)
        else:
            rightSubTree = BST(self.root.left)
            rightSubTree.insert(new_val)
        pass

    def search(self, find_val):
        if (self.root.value == find_val):
            return True
        elif(self.root.left != None):
            leftSubTree = BST(self.root.left)
            return leftSubTree.search(find_val)
        elif(self.root.right != None):
            rightSubTree = BST(self.root.right)
            return rightSubTree.search(find_val)
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        val = self.root.value
        sys.stdout.write('%s' %val)
        if(self.root.left != None):
            #print('going left')
            sys.stdout.write('-')
            lSubTree = BinaryTree(self.root.left)
            lSubTree.print_tree()
        if(self.root.right != None):
            #print('going right')
            sys.stdout.write('-')
            rSubTree = BinaryTree(self.root.right)
            rSubTree.print_tree()
        print('')
        return ""


# Set up tree
tree = BST(Node(4))

# Insert elements
#tree.print_tree()
tree.insert(2)
#tree.print_tree()
tree.insert(1)
#tree.print_tree()
tree.insert(3)
#tree.print_tree()
tree.insert(5)
#tree.print_tree()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)