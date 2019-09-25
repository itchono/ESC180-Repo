from math import sqrt


# ESC180 Lab 1
# Completed by Mingde Yin
# Connected Cows
# DO NOT modify any function or argument names

def find_euclidean_distance(x1, y1, x2, y2):
    """
    (float, float, float, float) -> float

    find_euclidean_distance calculates the Euclidean distance between two given 2D points
    P1(x1, y1) and P2(x2, y2) as a float rounded to 2 decimal places and returns it.
    The two points are inputted in sequence component-by component as 4 floats, in the sequence x1, y1, x2, y2.
    """
    # apply distance formula d = sqrt((x2-x1)^2 + (y2-y1)^2)
    # and also round to 2 d.p. using round function
    return round((sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)), 2)


def is_cow_within_bounds(cow_position, boundary_points):
    """
    (list<float>, list<list<float>>) -> int

    is_cow_within_bounds determines whether a cow is within the bounds or not given a cow’s position and
    the boundary points of the cow’s enclosure. The function returns an int value of 1 is the cow is within bounds
    or 0 if the cow is not.
    boundary_points must be inputted as a list of 4 nested lists, each containing 2 floats, denoting the
    x,y coordinates of a rectangular boundary starting from the upper left corner and moving clockwise.
    cow_position must be inputted as a list of 2 floats, denoting the x,y coordinates of the cow
    Assumes x+ is right and y+ is up.
    """
    # check cow's position:
    # upper statement: check whether cow's x coordinate fits between the x coordinates of points 0 and 1
    # lower statement: check whether cow's y coordinate fits between the y coordinates of points 0 and 3
    if (boundary_points[1][0] > cow_position[0] > boundary_points[0][0]) \
            and (boundary_points[0][1] > cow_position[1] > boundary_points[3][1]):
        # in the case where this is true return the positive result (1)
        return 1

    else:
        # the cow is not within bounds, thus return zero
        return 0


def find_cow_distance_to_boundary(cow_position, boundary_point):
    """
    (list<float>, list<float>) -> float

    find_cow_distance_to_boundary takes in two lists, cow_position and boundary_points, each containing two float
    values representing x,y coordinates and returns the distance between those specified points as a float rounded to
    2 d.p.
    NOTE: this function relies on find_euclidean_distance to round accurately.
    """
    return find_euclidean_distance(cow_position[0], cow_position[1], boundary_point[0], boundary_point[1])


def find_time_to_escape(cow_speed, cow_distance):
    """
    (float, float) -> float

    find_time_to_escape determines the time it will take for a cow to escape its enclosure given the float cow_speed
    representing the cow's speed and the float cow_distance representing the distance needed to escape.
    The value is returned as a float rounded to 2 d.p.

    IF cow_speed is equal to zero (or negative) the function returns -1 by default.
    """
    if cow_speed > 0:
        # for any valid speed (non zero)
        return round(cow_distance / cow_speed, 2)
    else:
        return -1


def report_cow_status(cow_position1, cow_position2, delta_t, boundary_points):
    """
    (list<float>, list<float>, float, list<list<float>>) -> float

    report_cow_status takes in:
    a set of coordinates, boundary_points, as a list of nested lists each with two floats
    corresponding to the x,y coordinates defining a rectangular boundary clockwise starting from the top left corner;
    two lists, cow_position1 and cow_position2 storing two floats each corresponding to the x,y position of a cow;
    delta_t, a float describing the time taken for a cow to travel between the two positions

    The function returns a float depending on the situation:
    - Returns shortest escape time from cow's second position IF cow is within bounds at both points and assuming
      it maintains its uniform velocity
    - Returns shortest time for cow to return to boundary point 0 IF the cow is out of bounds at both points and
      assuming it maintains its uniform velocity
    - Returns -1 if cow returns in bounds after being out of bounds
    - Returns 0 if cow escapes bounds (first point within and second point out of bounds)
    """
    # First, determine cow's speed, which will be useful later on
    # v = d/t
    cow_speed = find_euclidean_distance(cow_position1[0], cow_position1[1], cow_position2[0], cow_position2[1]) / delta_t

    # Break down into 4 cases are defined in the docstring

    # Case 1: Cow within bounds at both points --> measure escape time
    if bool(is_cow_within_bounds(cow_position1, boundary_points)) and \
            bool(is_cow_within_bounds(cow_position2, boundary_points)):
        escape_distances = {find_cow_distance_to_boundary(cow_position2, boundary_points[0]),
                            find_cow_distance_to_boundary(cow_position2, boundary_points[1]),
                            find_cow_distance_to_boundary(cow_position2, boundary_points[2]),
                            find_cow_distance_to_boundary(cow_position2, boundary_points[3])}
        # list out possible escape distances with all 4 boundary points
        # use min() function to return minimum of the 4 possibilities
        # plug into find_time_to_escape
        return find_time_to_escape(cow_speed, min(escape_distances))

    elif not bool(is_cow_within_bounds(cow_position1, boundary_points)) and not \
            bool(is_cow_within_bounds(cow_position2, boundary_points)):
        # plug cow_position2 and boundary point 0 into distance, then plug along with speed into find_time_to_escape
        return find_time_to_escape(cow_speed, find_cow_distance_to_boundary(cow_position2, boundary_points[0]))

    elif not bool(is_cow_within_bounds(cow_position1, boundary_points)) and \
            bool(is_cow_within_bounds(cow_position2, boundary_points)):
        # special case return -1
        return -1

    else:
        # cow escape thus return 0
        return 0


if __name__ == '__main__':
    # USED FOR TESTING ONLY; do not mark thanks
    print(find_euclidean_distance(3.0, 3.0, 2.0, 5.0), 2.24)  # should return 2.24
    print(find_euclidean_distance(5.0, 2.0, 4.0, 2.0), 1.0)  # should be 1.0

    print(is_cow_within_bounds([3, 3], [[2, 5], [5, 5], [5, 1], [2, 1]]), 1)
    print(is_cow_within_bounds([3, 3], [[4, 4], [5, 4], [5, 2], [4, 2]]), 0)

    print(find_cow_distance_to_boundary([3, 3], [2, 5]), 2.24)  # should return 2.24
    print(find_cow_distance_to_boundary([2, 2], [0, 1]), 2.24)  # should return 2.24

    print(find_time_to_escape(2.0, 8.0), 4.0)  # should return 4.0
    print(find_time_to_escape(9.0, 111.0), 12.33)  # should return 12.33

    print(report_cow_status ([3, 3], [4, 4], 10.0, [[2, 5], [5, 5], [5, 1], [2,1]]), 7.09)
    print(report_cow_status ([0, 0], [3, 7], 10.0, [[2, 5], [5, 5], [5, 1], [2,1]]), 2.94)
    print(report_cow_status ([0, 0], [3, 3], 10.0, [[2, 5], [5, 5], [5, 1], [2,1]]), -1)
    print(report_cow_status ([3, 3], [3, 6], 10.0, [[2, 5], [5, 5], [5, 1], [2,1]]), 0)
