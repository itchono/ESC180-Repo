import random

# ex 1
def Q1(db, grade):
    students = []
    for k in db.keys():
        if grade in db[k]:
            students.append(k)
    return students

def Q2(n):
    random.seed(10)

    nums = [0]*(n**2) # make list of nums from 1 to n^2

    for i in range(n**2):
        nums[i] = i+1

    arr = [[0]*n for i in range(n)]
    # generate matrix

    for x in range(n):
        for y in range(n):
            arr[x][y] = nums.pop(random.randint(0, len(nums) -1)) # remember randint is inclusive!

    for i in arr:
        print(i)

def Q3():
    num = -1

    vles = {True:0, False:0}

    while num != 0:
        num = int(input('Enter an integer: '))
        if num != 0:
            vles[num > 0] += 1
    print('You entered {} positive and {} negative values.'.format(vles[True], vles[False]))

def Q4(b):
    arr = [int(i) for i in list(str(b))]
    result = 0

    for i in range(len(arr)):
        result += 2**i * arr[i]

    print(result)

def Q5(n):
    pi = 0

    nextFactor = 1

    for i in range(n):
        pi += 4/nextFactor
        nextFactor = -(nextFactor + 2) if nextFactor > 0 else -(nextFactor - 2)

    return pi

def Q6():
    with open('grades.txt', 'r') as file:
        with open('new.txt', 'w') as outfile:
            print('ok')

if __name__ == '__main__':
    database = {'Mohamed':['A', 'A+', 'C', 'FZ', 'B-'], 'Cindy':['B', 'B', 'C', 'A', 'B'], 'Mustafa':['A', 'A+', 'A+', 'C', 'C'], 'Stefan':['FZ', 'B', 'B', 'C', 'C']}
    
    grade = input('Grade?\n')

    
    print(Q1(database, grade))

    Q2(5)

    Q3()

    Q4(1001)

    print(Q5(50000))



