# ESC180 Lab 2 pt 1
# Mingde Yin
# 1005904425

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

    >>>cross_product([2, 8], [1, 4, 3])
    [24, -6, 0]
    '''

    if (len(v) > 3 or len(w) > 3):
        return list([]) # error case
    else:
        # fix arrays if not satisfactory number of dimensions
        for i in range(0, 3):
            if len(v) <= i:
                v.append(0)
            if len(w) <= i:
                w.append(0)
            # add correct indices to v and w if it has 0, 1, 2 components
        # take cross product
        return [v[1] * w[2] - v[2] * w[1], v[2] * w[0] - v[0] * w[2], v[0] * w[1] - v[1] * w[0]]


def scalar_projection(v, w):
    '''
    (list<number>, list<number>) -> number

    scalar_projection returns the scalar projection of w onto v, where w and v are lists
    representing n-dimensional vectors.

    >>> scalar_projection([-2], [1.5])
    -1.5
    '''
    # use existing functions to expedite process
    return dot_product(v, w) / vector_length(v)

def vector_projection(v, w):
    '''
    (list<number>, list<number>) -> list<number>

    vector_projection returns a list representing the vector projection of w onto v,
    each of which are represented by n-dimensional input lists.

    >>> vector_projection([-2], [1.5])
    [1.5]
    '''

    s = scalar_projection(v, w)
    # get scalar projection
    u = unit_vector(v)
    # create unit vector

    for i in range(0, len(v)):
        u[i] *= s
        # multiply components
    return u


if __name__ == "__main__":
    # test your vector operations here
    print(vector_from_points([3, -1, 0], [10, 0, 1]))
    print(vector_length([3, 4]))
    print(angle_between([0, 1, 0, 1], [1, 3, 4, 5]))
    print(unit_vector([2, 1]))
    print(cross_product([2,8], [1,4,3]))
    print(cross_product( [1, 1, 1, 0], [1, 5.5]))
    print(cross_product([1, 1, 1], [5.5, 5.5, 5.5]))
    print(cross_product([], [2]))
    print(scalar_projection([-2], [1.5]))
    print(vector_projection([0, 3], [1.5, 2]))
