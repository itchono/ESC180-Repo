from math import sqrt
# ESC180 Lab 1
# Connected Cows
# DO NOT modify any function or argument names

def find_euclidean_distance(x1, y1, x2, y2):
    """
    (float, float, float, float) -> float
    find_euclidean_distance calculates the Euclidean distance between two given 2D points
    P1(x1, y1) and P2(x2, y2) as a float rounded to 2 decimal places and returns it.
    """
    # apply distance formula
    return round((sqrt((x2-x1)**2 + (y2-y1)**2)), 2) # and also round to 2 d.p.


def is_cow_within_bounds(cow_position, boundary_points):
    """
    (list<float>, list<list<float>>) -> int
    Given a cow’s position and the boundary points of the cow’s enclosure, is_cow_within_bounds
    determines whether the cow is within the bounds or not. If the cow is within the bounds,
    return 1. Otherwise, if the cow is out of bounds, return 0.
    boundary_points must be inputted as a list of 4 lists each containing 2 floats, each denoting the
    x,y coordinates of a rectangular boundary starting from the upper left corner and moving clockwise.
    cow_position must be inputted as a list of 2 floats, denoting the x,y coordinates of the cow
    Assumes x+ is right and y+ is up
    """
    if  (boundary_points[1][0] > cow_position[0] > boundary_points[0][0])\
    and (boundary_points[0][1] > cow_position[1] > boundary_points[3][1]):
        # verfy x condition is satisfied and also y condition
        return 1
    else:
        return 0
# TBD: comment more and verify x+ and y+

def find_cow_distance_to_boundary(cow_position, boundary_point):
    """
    Your docstring here
    """
    #function body


def find_time_to_escape(cow_speed, cow_distance):
    """
    Your docstring here
    """

if __name__ == "__main__":
    print(is_cow_within_bounds([3, 3], [[4, 4], [5, 4], [5, 2], [4, 2]]))
