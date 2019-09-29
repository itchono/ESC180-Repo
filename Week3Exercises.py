# Week 3 Exercises

import math

# ex 1
def change(m):
    m0 = m
    q = m//25
    m %= 25

    d = m//10
    m %= 10

    n = m//5
    m %= 5

    print(m0, "is equal to\n", q, "quarters\n", d, "dimes\n", n, "nickels\n", m, "pennies.")
    
# ex 2
def round_num():
    n = float(input("Enter float"))
    print(((10*n)//1)/10) # rudimentary truncation
    print(round(n, 1))

# ex 3
def trig():
    d = math.pi*float(input("Angle in degrees"))/180
    print(d)
    print("sin(", d, ") =", math.sin(d), "\ncos(", d, ") =", math.cos(d), "\ntan(", d, ") =",math.tan(d))
    
# ex 4
def cdn_change(m):
    m0 = m
    q = m//25
    m %= 25

    d = m//10
    m %= 10

    n = m//5
    m %= 5

    if (m >= 3):
        n += 1
    print(m0, "is equal to\n", q, "quarters\n", d, "dimes\n", n, "nickels\n")
    
if __name__ == "__main__":
    change(67)
    round_num()
    trig()
    cdn_change(69)
    
