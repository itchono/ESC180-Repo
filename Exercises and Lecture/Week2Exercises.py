# Week 2 Exercises - There is no week 1 btw

def exercise_1():
    print("I am going to love this course")


def exercise_2():
    # largest 3 digit number is 999
    largest_3 = 999
    # smallest 5 digit number is 10000
    smallest_5 = 10000

    print("Largest 3 digit number:", largest_3, "\nSmallest 5 digit number:", smallest_5,
          "\nSum:", (largest_3 + smallest_5))


def exercise_3():
    cost_1 = int(input("Cost?\n"))
    num_items = int(input("How many?\n"))
    print("Total cost is $", num_items * cost_1, sep='')


def exercise_4():
    c = float(input("Celsius temperature: "))
    print("Fahrenheit equivalent is:", c * 9 / 5 + 32)


def exercise_5():
    x = float(input("Input x: "))
    print("The value of y = 4x + 3 is", round((4 * x + 3),2))


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
