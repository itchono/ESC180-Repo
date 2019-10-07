# lecture 02 testing
# sept 9 2019 and sept 12, 2019

'''
syntax errors
ex. x = 2 + 3 + (1
'''

'''
functions:
'''

def fahrenheit_to_celsius(f):
    '''Fahrenheit to Celsius
    (Float) -> Float

    this function converts float fahrenheit temp to float celsius temp
    '''
    celsius = (f-32)*5/9 #conversion using given formula
    return celsius

def celsius_to_kelvin(c):
    '''
    (float) -> float

    this function converts float celsius temp to float kelvin temp
    '''
    k = c + 273.15
    return k

def fahrenheit_to_kelvin(f):
    '''
    (float) -> float

    this function converts float fahrenheit temp to float kelvin temp
    '''
    k= celsius_to_kelvin(fahrenheit_to_celsius(f))
    return k



#will now move to main method

if __name__ == "__main__":
    f = int(input("fahrenheit?\n"))
    print(f, "F is equal to", fahrenheit_to_celsius(f), "C, or", fahrenheit_to_kelvin(f), "K.")
    x = bob

