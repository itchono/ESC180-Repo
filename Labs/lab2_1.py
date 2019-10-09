from math import *


def vector_from_points(p1, p2):
    '''
    (list<number>, list<number>) -> list<number>

	vector_from_points returns an n-dimensional list corresponding to a vector represented by
    p2 at the tail and p1 at the tip. p1 and p2 are lists with the same number of dimensions as the output.
	
	>>>vector_from_points([0, 0], [1, 2])
	[1, 2]
    '''

    v = []  # initialize empty list for case n = 0

    for i in range(0, len(p1)):
        # use for loop to append each dimension of array as the difference in coordinates to a vector component
        v.append(p2[i] - p1[i])

    return v


def vector_length(v):
    '''
    (list<number>) -> float

    vector_length returns the magnitude of an n-dimensional vector represented by the list v.
    Returns -1 for an empty list.

    >>>vector_length([2,1])
    2.23606797749979
    '''

    if len(v) == 0:
        # empty list had length zero
        return -1
    else:
        mag_sum = 0
        for i in range(0, len(v)):
            # apply pythagorean theorem for n-dimensions
            mag_sum += (v[i] ** 2)
        return sqrt(mag_sum)


def angle_between(v, w):
    '''
    (list<number>, list<number>) -> number

    angle_between returns the angle, in degrees, between two input vectors with
    n-dimensions represented by the lists v and w.

    >>>angle_between([-1], [2])
    180.0
    '''
    # use cosine formula
    dot_p = 0
    for i in range(0, len(v)):
        dot_p += v[i] * w[i]
        # element by element multiplication to get dot product

    dot_p /= (vector_length(v) * vector_length(w)) # divide by magnitude

    angle = acos(dot_p)
    return (angle * 180 / pi) # convert from rad to degrees


def dot_product(v, w):
    '''
    (list<number>, list<number>) -> number

    dot_product returns the dot product for two vectors of n-dimensions represented
    by the lists v and w.

    >>>dot_product( [0, 1, 0, 1], [1, 3, 4, 5])
    8
    '''
    dot_p = 0
    for i in range(0, len(v)):
        dot_p += v[i] * w[i]
        # element by element multiplication to get dot product
    return dot_p


def unit_vector(v):
    '''
    (list<number>) -> list<number>

    unit_vector returns an n-element list representing a unit vector in
    the same direction as the input vector represented by the list v.
    Returns empty list if input is empty list.

    >>>unit_vector([2, 1])
    [0.8944271909999159, 0.4472135954999579]
    '''

    if len(v) == 0:
        # empty list has length zero
        return list([])
    else:
        rt_list = []

        # unit vector is vector components each divided by magnitude of vector

        for i in v:
            # use list iterable
            rt_list.append(i/vector_length(v))
        return rt_list


def cross_product(v, w):
    '''
    (list<number>, list<number>) -> list<number>

    cross_product returns a 3-element list representing v x w. If n < 3, the components
    are assumed to be given in order with the remaining elements set to zero. If n > 3 then
    an empty list is returned.

    TBD: EXAMPELS
    '''

    


def scalar_projection(v, w):
    ''' Fill in docstring
    '''


def vector_projection(v, w):
    ''' Fill in docstring
    '''


if __name__ == "__main__":
    # test your vector operations here
    print(vector_from_points([3, -1, 0], [10, 0, 1]))
    print(vector_length([3, 4]))
    print(angle_between([0, 1, 0, 1], [1, 3, 4, 5]))
    print(unit_vector([2, 1]))
