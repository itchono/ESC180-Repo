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
    The two points are inputted in sequence component-by component as 4 floats, in the sequence x1, y1, x2, y2
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
    Assumes x+ is right and y+ is up
    """
    # check cow's position:
    # upper statement: check whether cow's x coordinate fits between the x coordinates of points 0 and 1
    # lower statement: check whether cow's y coordinate fits between the y coodinates of points 0 and 3
    if (boundary_points[1][0] > cow_position[0] > boundary_points[0][0]) \
            and (boundary_points[0][1] > cow_position[1] > boundary_points[3][1]):
        # in the case where this is true return the positive result (1)
        return 1

    else:
        # the cow is not within bounds, thus return zero
        return 0


def find_cow_distance_to_boundary(cow_position, boundary_point):
    """
    Your docstring here
    """
    # function body


def find_time_to_escape(cow_speed, cow_distance):
    """
    Your docstring here
    """


if __name__ == "__main__":
    print(is_cow_within_bounds([3, 3], [[4, 4], [5, 4], [5, 2], [4, 2]]))
