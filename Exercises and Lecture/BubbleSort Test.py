#bubble sort

def bubblesort(arr):

    sorted = False #invoke bool

    while not sorted:
        sorted = True # assume sorted
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                #tuple swap
                arr[i+1], arr[i] = arr[i], arr[i+1]
                sorted = False


if __name__ == "__main__":
    arr = [6, 5, 4, 3 ,2, 1, 0]
    bubblesort(arr)
    print(arr)

    
