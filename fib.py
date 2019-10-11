def fibbonacci(n):
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

if __name__ == "__main__":
    n = int(input())
    print(fibbonacci(n))
    
 
