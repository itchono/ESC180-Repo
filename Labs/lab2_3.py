# ESC180 Lab 2 pt 3
# Mingde Yin
# 1005904425

# You may want to import your lab2_2 module

from lab2_2 import *

def dec_to_bin_list(dec_num):
    # DO NOT modify this function
    """
    (num)-> List[num]

    Function that converts decimal integer number to binary

    Usage: bin_list = dec_to_bin_list( dec_num )
    Input: dec_num is an integer number
    Output: bin_list is a list with four elements (0's and 1's), in the order of most significant bit to least significant bit

    The function assumes that dec_num is an integer.

    Inputs that are not in the range 0 to 15 will produce the same output as dec_num - 16*k where
    k is an integer that makes dec_num - 16*k attain a value from 0 to 15.

    >>> dec_to_bin_list(8)
    [1, 0, 0, 0]

    >>> dec_to_bin_list(16)
    [0, 0, 0, 0]
    """

    bin_list = []
    # start building the bin_list from the least significant bit
    # only need 4 bits
    while len(bin_list) < 4:
        curr_bit = dec_num % 2
        bin_list.append(int(curr_bit))
        dec_num = (dec_num - curr_bit)/2

    return list(reversed(bin_list))

def bin_list_to_dec(bin_list):
    # DO NOT modify this function
    '''
    (List[int]->int)

    Returns the decimal value of the input 4-bit number represented by bin_list.

    >>> bin_list_to_dec([1, 0, 0, 0])
    8
    '''
    dec = 0
    for i in range(len(bin_list)-1,-1, -1):
       dec += bin_list[i]*2**(len(bin_list)-i-1)
    return int(dec)

def add_two_bin_nums(four_bit_num1, four_bit_num2):
    '''
    (list<int>, list<int>) -> list<int>

    add_two_bin_nums returns the result of the binary addition of two four bit packets,
    four_bit_num1, four_bit_num2

    >>> add_two_bin_nums([1,1,1,0], [1,1,0,0])
    [1, 0, 1, 0]
    '''
    # ignore overflow bits

    result = [0, 0, 0, 0]
    for i in range(3, -1, -1):
        result[i] += four_bit_num1[i] + four_bit_num2[i]
        if (result[i] >= 2):
            if (i > 0):
                # allow overflow for 2^4 bit
                result[i-1] += 1
            result[i] -= 2
    return result
    # TBD

def check_bit_add(four_bit_num1, four_bit_num2, result):
    '''
    (list<int>, list<int>, list<int>) -> list<int>

    check_bit_add checks the result of 4 bit addition against the input list result.
    Error indices are returned as a list. If there are no errors, [] is returned

    >>>check_bit_add([1, 0, 1, 0],[0, 1, 0, 1], [0,1,0,1])
    [0, 2]
    '''

    # reuse existing functions to expedite process
    return error_indices(add_two_bin_nums(four_bit_num1, four_bit_num2), result)


def check_dec_add(four_bit_num1, four_bit_num2):
    '''
    (list<int>, list<int>) -> int

    check_dec_add checks if the bit addition of the two 4 bit inputs results in the same
    as the addition of decimals.

    Returns 0 if the bit addition result differs from correct decimal value
    Returns 1 if the bit addition does not differ

    >>> check_dec_add([0,0,1,1], [0,1,0,1])
    1
    '''

    # compare binary addition converted to decimal against sum of binaries converted to decimals
    # also, use int cast from boolean
    return int(bin_list_to_dec(add_two_bin_nums(four_bit_num1, four_bit_num2)) == \
               (bin_list_to_dec(four_bit_num1) + bin_list_to_dec(four_bit_num2)))


def get_error_source(four_bit_num1, four_bit_num2, result):
    '''
    (list<int>, list<int>, list<int>) -> list<int>

    get_error_source returns 0 if result yields the correct decimal value for addition
    returns 1 if bit overflow solely caused the error
    returns 2 if bit overflow did not solely cause the error ex. addition error.
    
    >>>get_error_source([1,0,0,1], [1,0,0,1], [1,0,1,0])
    2
    '''

    
    if (len(list(check_bit_add(four_bit_num1, four_bit_num2, result))) > 0):
        # Case: erroneous indices otherwise means incorrect addition
        # must be checked first as per test cases.
        return 2
    elif (check_dec_add(four_bit_num1, four_bit_num2) == 0):
        # Case: bit overflow, check_dec_add would return 0
        return 1
    else:
        # Case: decimal addition will be correct
        return 0


if __name__ == "__main__":
    # test your functions here
    # num 1 and num 2 should be positive integers less than 16
    '''
    four_bit_num1 = [1, 1, 1, 1]
    four_bit_num2 = [1,1,1,1]

    print((bin_list_to_dec(add_two_bin_nums(four_bit_num1, four_bit_num2)),\
               (bin_list_to_dec(four_bit_num1) + bin_list_to_dec(four_bit_num2))))
    
    '''
    
    print(get_error_source([1,0,0,1], [1,0,0,1], [1,0,1,0]))
    
    
    for dec1 in range(0, 16):
        for dec2 in range(0,16):
            bin1 = dec_to_bin_list(dec1)
            bin2 = dec_to_bin_list(dec2)
            print(dec1, dec2, get_error_source(bin1, bin2, dec_to_bin_list(dec1+ dec2)))
            if (get_error_source(bin1, bin2, dec_to_bin_list(dec1+ dec2)) != 0):
                print("Error dec1 = {} and dec2 = {} - result was {}".format(dec1, dec2, get_error_source(bin1, bin2, dec_to_bin_list(dec1+ dec2))))
    for dec1 in range(0, 16):
        for dec2 in range(0,16):
            bin1 = dec_to_bin_list(dec1)
            bin2 = dec_to_bin_list(dec2)
            if (get_error_source(bin1, bin2, [0, 0, 0, 0]) != 2):
                print("Error dec1 = {} and dec2 = {} - result was {}".format(dec1, dec2, get_error_source(bin1, bin2, dec_to_bin_list(dec1+ dec2))))
            if (get_error_source(bin1, bin2, dec_to_bin_list(dec1+ dec2)) == 2):
                print("2")
       
    
