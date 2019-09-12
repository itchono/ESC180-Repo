import lec02stuff
import random

if __name__ == "__main__":
    #let's learn about random
    sum = 0
    iterate = 1000
    for i in range(1, iterate):
        curr = (random.randint(0, 10))
        print(curr)
        sum += curr

    print(sum/iterate)
