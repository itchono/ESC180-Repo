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
    for i in range(0, 4):
        n = 3 - i
        result.insert(0, four_bit_num1[n] + four_bit_num2[n])
        if (n > 0):
            if (result[n] > 1):
                result[n] = 0
                result[n+1] += 1
    # TBD

def check_bit_add(four_bit_num1, four_bit_num2, result):
    ''' Fill in docstring
    '''

def check_dec_add(four_bit_num1, four_bit_num2):
    ''' Fill in docstring
    '''

def get_error_source(four_bit_num1, four_bit_num2, result):
    ''' Fill in docstring
    '''


if __name__ == "__main__":
    # test your functions here
    # num 1 and num 2 should be positive integers less than 16

    dec1 = int(input('Num 1: '))
    dec2 = int(input('Num 2: '))

    bin1 = dec_to_bin_list(dec1)
    bin2 = dec_to_bin_list(dec2)

    bin_result = add_two_bin_nums(bin1, bin2) # to test your add_two_nums

    # makes the answer sometimes incorrect (emulates a bug that is not solely due to bit overflow)
    bin_result.sort()

    # alternate method of messing up the result
    # bin_result = list(reversed(bin_result))

    dec_result = bin_list_to_dec(bin_result)

    print('{} + {} = {}'.format(dec1, dec2, dec_result))

    # for testing your get_error_source, you may wish to comment this section initially
    if dec_result != dec1 + dec2:
        error_source = get_error_source(bin1, bin2, bin_result)
        if error_source == 0:
            print('Correct')
        elif error_source == 1:
            print('Bit overflow error')
        elif error_source == 2:
            print('Addition error')
        else:
            print('Unknown error code')