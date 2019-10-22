import utilities


def rotate_90_degrees(image_array, direction=1):
    '''
    (list<image>, int) -> list<image>
    
    rotate_90_degrees takes in a list of length h (number of rows) with sublists of length w (number of columns)
    and returns a list with the same dimensions representing the image rotated 90 degrees
    either clockwise (1) or anticlockwise (-1).
    
    >>> rotate_90_degrees([[0, 0, 1],[0, 0, 1],[0, 0, 1]], 1)
    [[0,0,0], [0,0,0], [1,1,1]]
    '''

    (w, h) = (len(image_array[0]), len(image_array))
    # determine width and height of incoming image

    '''
    output_array = [[0]*w for i in range(h)]
    # USE THIS FOR 2D ARRAYS YOU BOT
    
    print("Width = {}, Height = {}".format(len(output_array[0]), len(output_array)))
    print("Width = {}, Height = {}".format(w, h))  # DEBUG ONLY
    
    # process row by row
    for y in range(0, h):
        for x in range(0, w):
            
            output_array[y][x] = image_array[y][x]
    '''
    # this will clone the image as-is

    output_array = [[0] * h for i in range(w)]
    # invert width and height = w lists of length h

    # process row by row
    if direction == -1:
        for y in range(0, h):
            for x in range(0, w):
                output_array[(w - 1) - x][y] = image_array[y][x]
                # remap each pixel to a rotated image CCW
    else:
        for y in range(0, h):
            for x in range(0, w):
                output_array[x][y] = image_array[(h-1)-y][x]
                # remap each pixel to a rotated image CW

    return output_array

def flip_image(image_array, axis=0):
    '''
        (list<image>, int) -> list<image>

        flip_image takes in a list with the same format as above
        and returns a list with the same dimensions representing the image flipped either
        vertically (1),  horizontally (0), or both (-1)

        >>> flip_image([[0, 0, 1],[0, 0, 1],[0, 0, 1]], 0)
        [[1,0,0], [1,0,0], [1,0,0]]
    '''
    # axis = -1 (along x = y), 0 along y, 1 along x

    (w, h) = (len(image_array[0]), len(image_array))
    # determine width and height of incoming image

    output_array = [[0] * w for i in range(h)]
    # create empty output template

    if axis == -1:
        for y in range(0, h):
            for x in range(0, w):
                output_array[(h - 1) - y][(w-1)-x] = image_array[y][x]
    elif axis == 1:
        for y in range(0, h):
            for x in range(0, w):
                output_array[(h - 1) - y][x] = image_array[y][x]
    else:
        for y in range(0, h):
            for x in range(0, w):
                output_array[y][(w - 1) - x] = image_array[y][x]

    return output_array


def crop(image_array, direction, n_pixels):
    #####################################
    ##########YOUR CODE GOES HERE########
    #####################################
    return output_array


def rgb_to_grayscale(rgb_image_array):
    #####################################
    ##########YOUR CODE GOES HERE########
    #####################################

    return output_array


def invert_rgb(image_array):
    #####################################
    ##########YOUR CODE GOES HERE########
    #####################################

    return output_array


def gaussian_blur(image_array, sigma=0.84089):
    #####################################
    ##########YOUR CODE GOES HERE########
    #####################################

    return output_array


def image_to_drawing(image_array):
    #####################################
    ##########YOUR CODE GOES HERE########
    #####################################

    return output_array


if (__name__ == "__main__"):
    file = 'robot.png'

    img = utilities.image_to_list("surprised_pikachu.png")
    '''
    utilities.write_image(rgb_to_grayscale(
        utilities.image_to_list(file)), 'gray.png')
    '''

    utilities.write_image(flip_image(img, 1), 'test.png')
