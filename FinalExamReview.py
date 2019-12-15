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
    clean = s.lower().replace(',', '').replace('!', '').replace('.', '')
    return clean.split(" ")

# Q6
def num_duplicates(d):
    dupes = 0
    for k in d:
        for other_key in d:
            if other_key != k and d[other_key] == d[k]:
                dupes += 1
                break
    return dupes

if __name__ == "__main__":
    print(count_upper_lower('IPv6 versus IPv4'))
    print(insertionSort([1,7,9,2,3,6,4,5,9]))
    print(highest_numbersmodded(genRand(10)))
    print(swap_in_place(92))
    print(transform_to_words("Hello! I am Jane."))
    print(num_duplicates({'Ellen':5,'Oprah':7,'Jimmy':5,'Stephen':5}))