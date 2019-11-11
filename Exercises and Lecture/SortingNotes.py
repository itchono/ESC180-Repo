# test of myself for sorting algorithms

import random

def bubblesort(arr):
    # Worse Case: O(n^2) swaps and O(n^2) comparisons
    # Base Case: O(1) swaps and O(n) comparisons
    # Average Case: n^2 and n^2

    comparisons = 0
    swaps = 0

    sorted = False
    i = 0 # pointer for top sorted portion

    while i < len(arr) and not sorted:
        sorted = True
        for j in range(0, len(arr)-1-i): # CARE: remember sorted partition at top of array
            comparisons += 1
            if arr[j] > arr[j+1]:
                sorted = False
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
                swaps += 1
        i += 1

    print('Bubblesort:\nLength: {}\nSwaps: {}\nComparisons: {}\n'.format(len(arr), swaps, comparisons))

def insertionsort(arr):
    # Worse Case: O(n^2) swaps and O(n^2) comparisons
    # Base Case: O(1) swaps and O(n) comparisons
    # Average Case: n^2 and n^2

    i = 0 # pointer for sorted partition

    comparisons = 0
    swaps = 0

    for i in range(len(arr)): # remember to use for loop as outside loop for sSort and iSort
        j = i

        while j > 0 and arr[j] < arr[j-1]: # the entire check exists in the WHILE loop
            comparisons += 1
            arr[j] , arr[j-1] = arr[j-1], arr[j]
            swaps += 1
            j -= 1

    print('Insertionsort:\nLength: {}\nSwaps: {}\nComparisons: {}\n'.format(len(arr), swaps, comparisons))

def selectionnsort(arr):
    # All Cases: O(n) swaps and O(n^2) comparisons

    i = 0 # pointer for sorted partition

    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        pos_min = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[pos_min]: # remember to use min position
                comparisons += 1
                pos_min = j
        arr[pos_min], arr[i] = arr[i], arr[pos_min]
        swaps += 1

    print('Selectionsort:\nLength: {}\nSwaps: {}\nComparisons: {}\n'.format(len(arr), swaps, comparisons))

if __name__ == "__main__":
    random.seed(1)

    l = 10

    nums = [random.randint(0, l*2) for i in range(l)] # remember this cool trick for populating arrays as well as [0] * n for single layer

    print('Starting Array: ', nums)

    bSort = nums[:]
    iSort = nums[:]
    sSort = nums[:]

    bubblesort(bSort)
    insertionsort(iSort)
    selectionnsort(sSort)

    print('BubbleSorted: ', bSort)
    print('InsertionSorted: ', iSort)
    print('SelectionSorted: ', sSort)

    

        