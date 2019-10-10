# ESC180 Lab 2 pt 1
# Mingde Yin
# 1005904425


def packet_size(packet):
    '''
    (list<int>) -> int

    packet_size returns the bit size of a packet represented by the list packet.

    >>> packet_size([0,1,0,1])
    4
    '''
    return len(packet)  # TBD what?


def error_indices(packet1, packet2):
    '''
    (list<int>, list<int>) -> list<int>

    error_indices returns a list containing the indices of the bit errors between
    packet1 and packet2.

    >>> error_indices([0,1,1,1], [1,1,0,1])
    [0, 2]
    '''

    err_list = []
    # initialize as empty

    for i in range(0, packet_size(packet1)):
        # noinspection PyRedundantParentheses
        if (packet1[i] != packet2[i]):
            # bit error
            err_list.append(i)

    return err_list


def find_packet_diff(packet1, packet2):
    '''
    (list<int>, list<int>) -> int

    packet_diff returns the number of bit errors between packet1 and packet2.

    >>> find_packet_diff([0,1,0,1], [1,1,0,1])
    1
    '''
    return len(error_indices(packet1, packet2))


if __name__ == "__main__":
    # test your bit error rate detector here
    print(find_packet_diff([0, 1, 0, 1], [1, 1, 0, 1]))
    print(error_indices([0, 1, 1, 1], [1, 1, 0, 1]))
