from math import sqrt

def vector_from_points(p1, p2):
    '''
	(list<float>, list<float>) -> list<float>
	
	vector_from_points returns an n-dimensional list corresponding to a vector represented by
	p2 at the tail and p1 at the tip. p1 and p2 are lists with the same number of dimensions.
	
	>>>vector_from_points([0, 0], [1, 2])
	[1, 2]
    '''
	
    v = [] # initialize empty list for case n = 0
	
    for i in range (0, len(p1)):
        v.append(p2[i] - p1[i])
		
    return v

def vector_length(v):
    ''' Fill in docstring
    '''

def angle_between(v, w):
    ''' Fill in docstring
    '''

def dot_product(v,w):
    ''' Fill in docstring
    '''

def unit_vector(v):
    ''' Fill in docstring
    '''

def cross_product(v,w):
    ''' Fill in docstring
    '''

def scalar_projection(v,w):
    ''' Fill in docstring
    '''

def vector_projection(v,w):
    ''' Fill in docstring
    '''

if __name__ == "__main__":
    # test your vector operations here
    v1 = [0, -2, 3]
    v2 = [1, 1, 1]
    print(vector_from_points(v1, v2))