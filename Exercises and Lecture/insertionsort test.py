# insertion sort

# partitioning of numbers

# start with a sorted partition with pointer, p

# in-place sort: no new array creation

# since we sort in-place, we bubble the element to tgt position

# Computational complexity of approx. n^2 for worse case (like bubble) n best case

def insertionsort(arr):
    for p in range(len(arr)):
        # everything to the left of P is sorted
        i = p
        while arr[i] < arr[i-1] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
        print(arr)
                


if __name__ == "__main__":
    arr = [6, 5, 4, 3 ,2, 1, 0]
    insertionsort(arr)
    print(arr)
    
