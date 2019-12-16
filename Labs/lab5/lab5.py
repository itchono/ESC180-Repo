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
        return str(self.data) # cast to string just to be sure

class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def insert_recursive(self, node, curr = None):
        try:
            if node.data <= curr.data:
                if curr.left is None:
                    curr.left = node # done
                else:
                    self.insert_recursive(node, curr.left)
            else:
                if curr.right is None:
                    curr.right = node # done
                else:
                    self.insert_recursive(node, curr.right)
        except AttributeError:
            # if curr node is None
            if not self.root is None:
                self.insert_recursive(node, self.root)
            else:
                self.root = node

    def insert(self, node):
        '''
        (instance method, Node) --> None

        Inserts the Node, node, into the corresponding position of the tree.
        '''
        if self.root != None:
            # make sure root exists
            currentNode = self.root
            previousNode = None

            while currentNode != None:
                # while node still exists along my current path, keep going
        
                previousNode = currentNode
                # node to left must be less than or equal, node to right must be greater
                if node.data > currentNode.data:
                    currentNode = currentNode.right
                else:
                    currentNode = currentNode.left
                # iteratively check next

            # insert node
            if node.data > previousNode.data:
                previousNode.right = node
            else:
                previousNode.left = node
        else:
            # if root does not exist, insert directly
            self.root = node

    def recursive_search(self, val, curr=None, rec=False):
        '''
        (instance method, str) --> bool

        Determines whether a string value, val exists within any node of the BST.

        tree.recursive_search("google.com")
        >>> true
        '''
        if not curr is None:
            if val < curr.data:
                return self.recursive_search(val, curr.left, rec=True)
            elif val > curr.data:
                return self.recursive_search(val, curr.right, rec=True)
            else:
                return True
        else:
            if not rec:
                return self.recursive_search(val, self.root, rec=True)
            else:
                return False


    def search(self, val):
        '''
        (instance variable, str) --> bool

        checks if the string, val, exists as a data value of a node in the tree.
        '''
        tStart = time.perf_counter() # define starting time

        currentNode = self.root
        found = (currentNode.data == val)

        while currentNode != None and not found:
            # node to left must be less, node to right must be greater
            # use this to determine our next 'move'
            if val > currentNode.data:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left

            try:
                # speed up searching using try/catch
                found = (currentNode.data == val)
            except AttributeError:
                found = False
        
        print('Elapsed Time: {:.3f} ms'.format((time.perf_counter() - tStart)*1000))
        return found

        # findings: Searching is incredibly fast.

def constructBST(filename):
    '''
    (str) --> BinarySearchTree

    takes in filename, reads strings, and inserts into a binary search tree, returning it afterward.
    '''
    with open(filename) as f:
        vals = f.read().strip('\n').split('\n') # clean up input

        tree = BinarySearchTree(None)
        # empty tree

        res = input("(R/I)?")

        rec = res.lower() == 'r'

        if rec:
            for i in range(0, len(vals)):
                # insert values directly
                tree.insert_recursive(Node(vals[i]))
        else:
            for i in range(0, len(vals)):
                # insert values directly
                tree.insert(Node(vals[i]))

        return tree
    
if __name__ == "__main__":

    tree = constructBST('websites.txt')

    print(tree.recursive_search('googole.com'))
    