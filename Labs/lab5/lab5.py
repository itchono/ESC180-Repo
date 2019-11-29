# ESC180 Lab 5
# Mingde Yin
# 1005904425

import time

class Node:
    # implement basic Node class
    def __init__(self, data='', left=None, right=None):
        # initialize instance variables
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        '''
        (instance method) --> str

        overloads the built in str() method and returns string with the value of the node.
        '''
        return self.data

class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def insert(self, node):
        '''
        (instance method, Node) --> None

        Inserts the Node, node, into the corresponding position of the tree.
        '''
        currentNode = self.root
        previousNode = None

        while currentNode != None:
            # while node still exists along my current path, keep going
    
            previousNode = currentNode
            # node to left must be less than or equal, node to right must be greater
            if str(node) > str(currentNode):
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
            # iteratively check next

        # insert node
        if str(node) > str(previousNode):
            previousNode.right = node
        else:
            previousNode.left = node
    
    def search(self, val):
        '''
        (instance variable, str) --> bool

        checks if the string, val, exists as a data value of a node in the tree.
        '''
        tStart = time.perf_counter() # define starting time

        currentNode = self.root
        found = (str(currentNode) == val)

        while currentNode != None and not found:
            # node to left must be less, node to right must be greater
            # use this to determine our next 'move'
            if val > str(currentNode):
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left

            found = (str(currentNode) == val)
        
        print('Elapsed Time: {:.3f} ms'.format((time.perf_counter() - tStart)*1000))
        return found

def constructBST(filename):
    '''
    (str) --> BinarySearchTree

    takes in filename, reads strings, and inserts into a binary search tree, returning it afterward.
    '''
    with open(filename) as f:
        vals = f.read().strip('\n').split('\n') # clean up input

        tree = BinarySearchTree(Node(vals[0]))
        # begin with first link as root

        for i in range(1, len(vals)):
            # insert the rest directly
            tree.insert(Node(vals[i]))

        return tree
    
if __name__ == "__main__":

    tree = constructBST('websites.txt')

    print(tree.search("google.com"))
