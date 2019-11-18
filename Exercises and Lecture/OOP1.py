import math

class Rectangle:

    # CONSTRUCTOR - 1st param in constructor is the self pointer; called implicitly! All subsequenct args are inputted at assignment
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


    # INSTANCE METHOD - same as constructor; must ALWAYS specify self pointer in args
    def area(self):
        return self.w * self.h

    def diag_dist(self):
        return math.sqrt(self.w ** 2 + self.h **2)

    def crop(self, dx=1, dy=1, ax=0, ay=0):
        '''
        Modifies a dimension of the rectangle in the directions chosen by the amounts chosen
        '''
        return Rectangle(self.x, self.y, self.w+ax*dx, self.h +ay*dy)

    def __str__(self):
        return ('Rectangle\nLeft: {0}\nBottom: {1}\nWidth: {2}\nHeight: {3}'.format(self.x, self.y, self.w, self.h))

    
if __name__ == "__main__":
    r = Rectangle(0,0,10, 9)
    print(r)
 
    print(r.area())
    print(r.diag_dist())

    print(r.crop(ax=10))

