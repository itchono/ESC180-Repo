# I will write my first function here
def fahrenheit_to_celsius(fahrenheit):
    '''
    (float) -> float
    :param fahrenheit:
    :return: returns the celsius equivalent
    '''

    return (fahrenheit-32)*5/9
    # uses 5/9 and 32 conversion to transform into degrees celsius

def celsius_to_kelvin(c):
    '''
    (float) -> float
    :param c:
    :return: kelvin
    '''

    return c + 273.15

def fahrenheit_to_kelvin(f):
    '''

    :param f:
    :return: kelvin
    '''
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

if __name__ == "__main__":
    # main code goes here
    print("HYELLO AND WELCOME TO GLORIOUS TEMPERATURE CONVERSION PROGRAM\n")
    initial_temp = float(input("(Step 1 of 3) Please enter the numerical value of the temperature you want to convert:\n"))
    # take in the initial temperature as a numeric value, cast to float type from string
    initial_unit = input("(Step 2 of 3) Please enter the unit of your temperature [C/F]:\n").capitalize()

    final_unit = input("(Step 3 of 3) Please enter the unit which you wish to convert to [C/F/K]:\n").capitalize()

    valid_units = {"C", "F", "K"}

    if (initial_unit not in valid_units) or (final_unit not in valid_units):
        # failsafe
        print("Error parsing units. Please try again with C, F or K.")
    else:
        final_temp = 0
        # initialize final temperature variable

        # cases junction
        if initial_unit == final_unit:
            # trivial case
            final_temp = initial_temp

        # followed by other cases
        # using nested selection for clarity
        elif initial_unit == "C":
            if final_unit == "K":
                final_temp = celsius_to_kelvin(initial_temp)
            elif final_unit == "F":
                final_temp = 0
        elif initial_unit == "F":
            if final_unit == "K":
                final_temp = fahrenheit_to_kelvin(initial_temp)
            elif final_unit == "C":
                final_temp = fahrenheit_to_celsius(final_temp)
        else:
            final_temp = 0

        print(initial_temp, initial_unit, " is equal to ", final_temp, final_unit, ".", sep="")

        # hello
