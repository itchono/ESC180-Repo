#import TemperatureApp
# or
from TemperatureApp import *

def convert_temperature(t, ui, uf):
    '''
    (float, str, str) --> float

    converts from a temperature scale to another

    given u, the input temperature as a numeric value

    ui, as the input unit
    uf, as the output unit

    ui, uf can take on C, F, K as values
    '''

    if ui == uf:
        # if you have the same units, just spit out the OG value
        return t
    elif ui == 'F':
        if uf == 'C':
            return fahrenheit_to_celsius(t)
        elif uf == 'K':
            return fahrenheit_to_kelvin(t)
        else:
            print("ERROR at junction - invalid units")
            return -1;
    elif ui == 'C':
        if uf == 'K':
            return celsius_to_kelvin(t)
        else:
            print("ERROR at junction - invalid units")
            return -1;
    else:
        print("ERROR at junction - invalid units")
        return -1;


if __name__ == "__main__":
    print("HYELLO AND WELCOME TO GLORIOUS TEMPERATURE CONVERSION PROGRAM\n")
    initial_temp = float(input("(Step 1 of 3) Please enter the numerical value of the temperature you want to convert:\n"))
    # take in the initial temperature as a numeric value, cast to float type from string
    initial_unit = input("(Step 2 of 3) Please enter the unit of your temperature [C/F/K]:\n").capitalize()

    valid_iu = {'C', 'F', 'K'}

    valid_fu = ({'F':{'C','F','K'}, 'C':{'C', 'K'}, 'K':{'K'}}) #cool dictionary trick

    print("(Step 3 of 3) Please enter the unit which you wish to convert to [",valid_fu[initial_unit], sep='', end='')

    final_unit = input("]:\n").capitalize()


    if initial_unit in valid_iu and final_unit in valid_fu[initial_unit]:
        print (initial_temp, initial_unit, "is equal to", convert_temperature(initial_temp, initial_unit, final_unit), final_unit, ".")
    else:
        print("Invalid unit combination.")

    
    
