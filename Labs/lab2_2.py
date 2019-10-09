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
    return len(packet)
    # TBD what?

def error_indices(packet1, packet2):
    '''
    (list<int>) -> int
    '''

def packet_diff(packet1, packet2):
    ''' Fill in docstring
    '''

if __name__ == "__main__":
    # test your bit error rate detector here
    packet_sent = [0, 1, 1, 1]
    packet_received = [1, 1, 1, 1]