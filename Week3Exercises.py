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
    n = float(input("Enter float\n"))
    print((n*10)//1 / 10) # rudimentary truncation
    print(round(n, 1))
	

# ex 3
def trig():
    d = math.pi*float(input("Angle in degrees\n"))/180
    print(round(d * 180 / math.pi, 2))
    print("sin(", round(d * 180 / math.pi, 2), ") =", math.sin(d), "\ncos(", round(d * 180 / math.pi, 2), ") =", math.cos(d), "\ntan(", round(d * 180 / math.pi, 2), ") =",math.tan(d), sep = '')
    
# ex 4
def cdn_change(m):
    m0 = m
	
	# round to nearest 5
    m = m0//5 * 5 + round(m0%5/5)
	
    q = m//25
    m %= 25

    d = m//10
    m %= 10

    n = m//5
    m %= 5
		
    print(m0, "is equal to\n", q, "quarters\n", d, "dimes\n", n, "nickels\n", "if you're in Canada.")
	
    
    
if __name__ == "__main__":
    change(67)
    round_num()
    trig()
    cdn_change(92)
    
