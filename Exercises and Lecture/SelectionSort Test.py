# selection sort

# much more comparisons but fewer swaps

# computational complexity is n^2

def selectionsort(arr):
    for p in range(0, len(arr)):
        i_min = p
        for i in range(p+1, len(arr)):
            if (arr[i] < arr[i_min]):
                i_min = i

        arr[p], arr[i_min] = arr[i_min], arr[p]
        print(arr)



if __name__ == "__main__":
    arr = [6, 5, 4, 3 ,2, 1, 0]
    selectionsort(arr)
    print(arr)
