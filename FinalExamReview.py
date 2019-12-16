import random

# Q1
def count_upper_lower(s):

    u = 0
    l = 0

    for c in s:
        if c.isupper():
            u += 1
        elif c.islower():
            l += 1
    return (u, l) # tuple return oooo

# Q2
def highest_numbers(arr):
    return (sorted(arr)[-1::-1])[0:5] # Quick tip: List reversal and slicing

def insertionSort(arr):
    for i in range(1, len(arr)):
        # denoting position of next extract
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1] # tuple-wise swap
            j -= 1
    return arr

def selectionSort(arr):
    for i in range(0, len(arr)-1):
        minPos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minPos]:
                minPos = j
        arr[minPos], arr[i] = arr[i], arr[minPos]

    return arr

def bubbleSort(arr):
    
    sorted = False
    i = 0

    while i < len(arr) and not sorted:
        sorted = True

        for j in range(len(arr)-1-i):
            if arr[j+1] < arr[j]:
                sorted = False
                arr[j+1], arr[j] = arr[j], arr[j+1]
        i += 1  
    return arr

def highest_numbersmodded(arr):
    return (sorted(arr)[-1::-1])[0:5] # Quick tip: List reversal and slicing


def genRand(length):
    return [random.randint(0, 1000) for i in range(length)]

# Q3
def squared_n(n):
    d = {} # note {} cannot be used for empty set, rather use set()
    for i in range(1, n+1):
        d[i] = i**2
    return d

# Q4
def swap_in_place(n):
    return (n%10) * 10 + n//10

# Q5
# String manipulation review
def transform_to_words(s):
    clean = ''
    for c in s:
        if c == ' ' or c.isalpha():
            clean += c.lower()
    return clean.split()

# Q6
def num_duplicates(d):
    # interesting alt solution

    dupes = 0
    vals = []
    for k in d:
        if not d[k] in vals:
            vals.append(d[k])
            locald = False
            for other_key in d:
                if other_key != k and d[other_key] == d[k]:
                    locald = True
            if locald:
                dupes += 1
    return dupes


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
        
        return found

        # findings: Searching is incredibly fast.

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

def insTree(t, L):
    if not L == []:
        t.insert(Node(L[len(L)//2]))
        insTree(t, L[0:len(L)//2])
        insTree(t, L[len(L)//2+1:])

if __name__ == "__main__":
    print(count_upper_lower('IPv6 versus IPv4'))
    print(insertionSort([1,7,9,2,3,6,4,5,9]))
    print(highest_numbersmodded(genRand(10)))
    print(swap_in_place(92))
    print(transform_to_words("Hello! I am Jane."))
    print(num_duplicates({'Ellen':5,'Oprah':7,'Jimmy':5,'Stephen':5}))


    print(selectionSort(genRand(20)))
    print(insertionSort(genRand(20)))
    print(bubbleSort(genRand(20)))

    '''
    tree = BinarySearchTree(None)
    nums = insertionSort(genRand(7))

    insTree(tree, nums)
    '''

