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
        # overload to_string method
        return self.data

class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def insert(self, node):
        
        currentNode = self.root
        previousNode = None

        while currentNode != None:
            # while node still exists along my current path, keep going
    
            previousNode = currentNode
            # node to left must be less, node to right must be greater
            if str(node) < str(currentNode):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
            # recursively check next

        # insert node after finishing (we found an empty space to put me)
        if str(node) < str(previousNode):
            previousNode.left = node
        else:
            previousNode.right = node
    
    def search(self, val):
        tStart = time.perf_counter() # define starting time

        currentNode = self.root
        found = (str(currentNode) == val)

        while currentNode != None and not found:
            # node to left must be less, node to right must be greater
            # use this to determine our next 'move'
            if val < str(currentNode):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

            found = (str(currentNode) == val)
        
        tEnd = time.perf_counter()

        
        tElapsed = tEnd - tStart
        
        print('Elapsed Time: {:.3f} ms'.format(tElapsed*1000))
        return found

def constructBST(filename):
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

    print(tree.search("zzzz8.cn"))
