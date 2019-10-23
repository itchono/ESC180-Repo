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
    for y in range(0, h):
        for x in range(0, w):
            # determine direction of rotation
            if direction == -1:
                output_array[(w - 1) - x][y] = image_array[y][x]
                # remap each pixel to a rotated image CCW
            else:
                output_array[x][y] = image_array[(h - 1) - y][x]
                # remap each pixel to a rotated image CW

    return output_array


def invert_greyscale(image_array):
    '''
    (list<image, greyscale>) -> list<image, greyscale>

    invert_greyscale takes in a list representing a *greyscale image*
    and returns it with all pixels inverted in colour

    See spec doc for example
    '''
    (w, h) = (len(image_array[0]), len(image_array))
    # determine width and height of incoming image

    output_array = [[0] * w for i in range(h)]
    # create empty output template

    for y in range(0, h):
        for x in range(0, w):
            output_array[y][x] = 255 - int(image_array[y][x])
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
    for y in range(0, h):
        for x in range(0, w):
            # determine axis of reflection
            if axis == -1:
                output_array[(h - 1) - y][(w - 1) - x] = image_array[y][x]
            elif axis == 1:
                output_array[(h - 1) - y][x] = image_array[y][x]
            else:
                output_array[y][(w - 1) - x] = image_array[y][x]

    return output_array


def crop(image_array, direction, n_pixels):
    '''
    (list<image>, string, int) -> list<image>

    crop takes in a list with the same format as above
    and returns a list with the the image cropped according to
    a direction (‘left’/‘right’/‘up’/‘down’) by n pixels

    >>> flip_image([[0, 0, 1],[0, 0, 1],[0, 0, 1]], 0)
    [[1,0,0], [1,0,0], [1,0,0]]
    '''

    (w, h) = (len(image_array[0]), len(image_array))
    # determine width and height of incoming image

    # respecifying params for output array
    if direction == 'left' or direction == 'right':
        w -= n_pixels
    else:
        h -= n_pixels

    output_array = [[0] * w for i in range(h)]
    # create empty output template

    for y in range(0, h):
        for x in range(0, w):
            if direction == 'left':
                output_array[y][x] = image_array[y][x + n_pixels]
            elif direction == 'down':
                output_array[y][x] = image_array[y + n_pixels][x]
            else:
                output_array[y][x] = image_array[y][x]

    return output_array


def rgb_to_grayscale(rgb_image_array):
    '''
    (list<image>) -> list<image, greyscale>

    rgb_to_greyscale converts the given RGB image to a Grayscale image using the formula
    𝑔𝑟𝑎𝑦 = 0.2989 ∗ 𝑟 + 0.5870 ∗ 𝑔 + 0.1140 ∗ b

    See spec doc for examples
    '''

    (w, h) = (len(rgb_image_array[0]), len(rgb_image_array))
    # determine width and height of incoming image

    output_array = [[0] * w for i in range(h)]
    # create empty output template

    for y in range(0, h):
        for x in range(0, w):
            output_array[y][x] = 0.2989 * rgb_image_array[y][x][0] + 0.5870 * rgb_image_array[y][x][1] + \
                                 0.1140 * rgb_image_array[y][x][2]

    return output_array


def invert_rgb(image_array):
    '''
    (list<image, greyscale>) -> list<image, greyscale>

    invert_rgb takes in a list representing an rgb image
    and returns it with all pixels inverted in colour

    See spec doc for example
    '''
    (w, h) = (len(image_array[0]), len(image_array))
    # determine width and height of incoming image

    output_array = [[[0] * 3 for j in range(w)] for i in range(h)]
    # create empty output template in rgb pixel format for faster operation

    for y in range(0, h):
        for x in range(0, w):
            for c in range(0, 3):
                # loop 3 times for each colour channel
                output_array[y][x][c] = 255 - int(image_array[y][x][c])
    return output_array


def gaussian_blur(image_array, sigma=0.84089, convolution_size=3):
    '''
    (list<image>, float, int) -> list<image>

    gaussian_blur takes in an image list and outputs the gaussian blurred image

    See spec doc for examples
    '''

    # generate convolution matrix

    ### tentative

    pi = 3.1415926535897
    e = 2.7182818284

    cm = [[0] * convolution_size for i in range(convolution_size)]

    for x in range(0, convolution_size):
        for y in range(0, convolution_size):
            cm[x][y] = 1 / (2 * pi * sigma) * e ** (-(x ** 2 + y ** 2) / (2 * sigma ** 2))
    print(cm)
    print("not yet implemented")


def image_to_drawing(image_array):
    #####################################
    ##########YOUR CODE GOES HERE########
    #####################################

    print("not yet implemented")


def brightness_contrast_gamma(image_array, alpha, beta, gamma):
    '''
    (list<image>, float, float, float) -> image<list>
    '''

    (w, h) = (len(image_array[0]), len(image_array))
    # determine width and height of incoming image

    output_array = [[[0] * 3 for j in range(w)] for i in range(h)]
    # create empty output template in rgb pixel format for faster operation

    for y in range(0, h):
        for x in range(0, w):
            for c in range(0, 3):
                # loop 3 times for each colour channel
                # b/c correction
                output_array[y][x][c] = alpha*int(image_array[y][x][c]) + beta
                if  output_array[y][x][c] > 255:
                    output_array[y][x][c] = 255
                elif output_array[y][x][c] < 0:
                    output_array[y][x][c] = 0

                output_array[y][x][c] = ((int(image_array[y][x][c])/255)**gamma) * 255
                if  output_array[y][x][c] > 255:
                    output_array[y][x][c] = 255
                elif output_array[y][x][c] < 0:
                    output_array[y][x][c] = 0

    return output_array


if (__name__ == "__main__"):
    file = 'surprised_pikachu.png'

    img = utilities.image_to_list("surprised_pikachu.png")

    grey = rgb_to_grayscale(img)
    '''
    utilities.write_image(rgb_to_grayscale(
        utilities.image_to_list(file)), 'gray.png')
    '''

    utilities.write_image(brightness_contrast_gamma(img, 1, 0, 0.8), 'test.png')
    # gaussian_blur(img)
