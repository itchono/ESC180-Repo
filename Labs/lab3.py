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
    
    # New constraint: square image

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


def histogram_equalization(img_array):
    '''
    (list<image>) -> list<image>
    
    histogram_equalization takes in an image list of a greyscale image and equalizes it using a histogram.
    
    See spec doc for examples
    '''
    
    (w, h) = (len(img_array[0]), len(img_array))
    # determine width and height of incoming image

    output_array = [[0] * w for i in range(h)]
    # create empty output template
    
    greys = [0]*256
    # create frequency matrix for image
    
    for y in range(0, h):
        for x in range(0, w):
            greys[int(img_array[y][x])] += 1
            # count frequency of greys
 
    cumulative_sum = [0]*256
    
    for i in range(0, 256):
        # create cumulative sum
        cumulative_sum[i] = cumulative_sum[i-1] + greys[i]
        
    for i in range(0, 256):
        # normalize from 0 to 255
        cumulative_sum[i] /= ((w*h)/255)
        
    for y in range(0, h):
        for x in range(0, w):
            output_array[y][x] = cumulative_sum[int(img_array[y][x])]
            # apply filter
    
    return output_array


if (__name__ == "__main__"):
    #file = 'surprised_pikachu.png'

    img = utilities.image_to_list("Specimen.jpg")

    grey = rgb_to_grayscale(img)
    '''
    utilities.write_image(rgb_to_grayscale(
        utilities.image_to_list(file)), 'gray.png')
    '''
    
    sample_grey = [[2,3,4,5], [0, 0, 0, 0], [1, 7, 3, 8], [6, 9, 4, 2]]
    sample_rgb = [[[42, 41, 40], [50, 49, 48], [96, 95, 94]], [[1, 1, 1], [2, 2, 2], [3,3,3]], [[4,4,4], [5,5,5], [6,6,6]]]
    
    output = crop(sample_grey, 'down', 1)
    rgbtest = rotate_90_degrees(invert_rgb(sample_rgb),-1)
    
    
    for i in sample_grey:
        print(i)
    print("\n")
    for i in output:
        print(i)
        
    for i in rgbtest:
        print(i)

    histogram_equalization(grey)
    utilities.write_image(rotate_90_degrees(img, -1), 'cool.png')
    utilities.write_image(histogram_equalization(grey), 'histogram.png')
