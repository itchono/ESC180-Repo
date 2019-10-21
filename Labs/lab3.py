import utilities

def rotate_90_degrees(image_array, direction = 1):
    '''
    (list<image>, int) -> list<image>
    
    rotate_90_degrees takes in a list of length h (number of rows) with sublists of length w (number of columns)
    and returns a list with the same dimensions representing the image rotated 90 degrees
    either clockwise (1) or anticlockwise (-1).
    
    >>> rotate_90_degrees([[0, 0, 1],[0, 0, 1],[0, 0, 1]], 1)
    [[0,0,0], [0,0,0], [1,1,1]]
    '''
    
    (w,h) = (len(image_array), len(image_array[0]))
    # determine width and height
    
    output_array = [[0]*w]*h
    
    for x in range(0, w):
        for y in range(0, h):
            output_array[x][y] = image_array[x][y]
    
    
   

	
    return output_array

def flip_image(image_array, axis = 0):
	#axis = -1 (along x = y), 0 along y, 1 along x
	
	#####################################
	##########YOUR CODE GOES HERE########
	#####################################
			
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
    
    utilities.write_image(rotate_90_degrees(img), 'test.png')
    
