def fib(n, t1=1, t2=1):
    if n<3:
        return [t1, t2][n-1]

    arr = []
    arr.append(t1)
    arr.append(t2)

    for i in range(3, n+1):
        arr.append((arr[i-2] + arr[i-3]))

    return arr[n-1]


def fibOG(n, t1=1, t2=1):
    if n < 3:
        return [t1, t2][n-1]

    arr = [0]*n
    arr[0:2] = [t1,t2]

    for i in range(3, n+1):
        arr[i-1] = (arr[i-2] + arr[i-3])

    return arr[n-1]

