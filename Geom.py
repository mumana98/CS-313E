#  File: Geom.py

#  Description: Point and Line classes

#  Student Name: Matthew Umana

#  Student UT EID: msu245

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 02/11/20

#  Date Last Modified: 02/14/20

import math

class Point (object):
  # constructor with default values
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
  # get distance to other which is another Point object
    def dist (self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
  # create a string representation of a Point (x, y)
    def __str__ (self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
  # test for equality between two points
    def __eq__ (self, other):
        tol = 1.0e-6
        return (abs (self.x - other.x) < tol and abs (self.y - other.y) < tol)
    
class Line (object):
  # line is defined by two Point objects p1 and p2
  # constructor assign default values if user does not define
  # the coordinates of p1 and p2 or the two points are the same
    def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
        self.p1_x = p1_x
        self.p1_y = p1_y
        self.p2_x = p2_x
        self.p2_y = p2_y

  # returns True if the line is parallel to the x axis 
  # and False otherwise
    def is_parallel_x (self):
        if is_equal(self.p1_y, self.p2_y):
            return True
        else:
            return False
  # returns True if the line is parallel to the y axis
  # and False otherwise
    def is_parallel_y (self):
        if is_equal(self.p1_x, self.p2_x):
            return True
        else:
            return False
  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
    def slope (self):
        return (self.p2_y - self.p1_y)/(self.p2_x - self.p1_x)


  # determine the y-intercept of the line
  # return None if line is parallel to the y axis
    def y_intercept (self):
        return self.p1_y-(self.slope()*self.p1_x)
        

  # determine the x-intercept of the line
  # return None if line is parallel to the x axis
    def x_intercept (self):
        return (-self.y_intercept())/self.slope()

  # returns True if line is parallel to other and False otherwise
    def is_parallel (self, other):
        if is_equal(self.slope(), other.slope()):
            return True
        else:
            return False 

  # returns True if line is perpendicular to other and False otherwise
    def is_perpendicular (self, other):
        if is_equal((-1/self.slope()), other.slope()):
            return True
        else:
            return False

  # returns True if Point p is on the line or an extension of it
  # and False otherwise
    def is_on_line (self, p):
        if is_equal(p.y, (self.slope()*p.x)+self.y_intercept()):
            return True
        else:
            return False
        
  # determine the perpendicular distance of Point p to the line
  # return 0 if p is on the line
    def perp_dist (self, p):
        return abs((self.p2_x-self.p1_x)*(self.p1_y-p.y) - (self.p1_x-p.x)*(self.p2_y-self.p1_y)) / math.sqrt((self.p2_x-self.p1_x)**2 + (self.p2_y-self.p1_y)**2)


  # returns a Point object which is the intersection point of line
  # and other or None if they are parallel
    def intersection_point (self, other):
        inter_y = (other.slope() / self.slope()) + other.y_intercept() + (-self.y_intercept())
        inter_x= (self.slope() * inter_y + self.y_intercept())
        return inter_x, inter_y

  # return True if two points are on the same side of the line
  # and neither points are on the line
  # return False if one or both points are on the line or both 
  # are on the same side of the line
    def on_same_side (self, p1, p2):
        determine1 = (p1.x-self.p1_x) * (self.p2_y-self.p1_y) - (p1.y-self.p1_y) * (self.p2_x-self.p1_x)
        otherpoint = (p2.x-self.p1_x) * (self.p2_y-self.p1_y) - (p2.y-self.p1_y) * (self.p2_x-self.p1_x)
        if (determine1 > 0 and otherpoint > 0) or (determine1 < 0 and otherpoint < 0) and ((self.is_on_line(p1) == False) and (self.is_on_line(p2) == False)):
            return True
        else:
            return False

  # string representation of the line - one of three cases
  # y = c if parallel to the x axis
  # x = c if parallel to the y axis
  # y = m * x + b
    def __str__ (self):
        if self.is_parallel_y():
            return "y = " + str(self.y_intercept())
        elif self.is_parallel_x():
            return "x = " + str(self.x_intercept())
        else:
            return "y = " + str(self.slope()) + "x" + " + " + str(self.y_intercept())

def is_equal (a, b):
    tol = 1.0e-6
    return (abs (a - b) < tol)

def main():
    # open file "geom.txt" for reading
    in_file = open("geom.txt", "r")
    
    # read the coordinates of the first Point P
    line = in_file.readline()
    line = line.strip()
    line = line.split()
    p_x = float(line[0])
    p_y = float(line[1])
    P = Point(p_x, p_y)
    # read the coordinates of the second Point Q
    line = in_file.readline()
    line = line.strip()
    line = line.split()
    q_x = float(line[0])
    q_y = float(line[1])
    Q = Point(q_x, q_y)
    # print the coordinates of points P and Q
    print("Coordinates of P:", P)
    print("Coordinates of Q:", Q)
    # print distance between P and Q
    print("Distance between P and Q:", P.dist(Q))
    
    # print the slope of the line PQ
    PQ = Line(P.x,P.y,Q.x,Q.y)
    print("Slope of PQ:", PQ.slope())
    
    # print the y-intercept of the line PQ
    print("Y-Intercept of PQ:", PQ.y_intercept())
    
    # print the x-intercept of the line PQ
    print("X-Intercept of PQ:", PQ.x_intercept())
    
    # read the coordinates of the third Point A
    line = in_file.readline()
    line = line.strip()
    line = line.split()
    a_x = float(line[0])
    a_y = float(line[1])
    A = Point(a_x, a_y)
    
    # read the coordinates of the fourth Point B
    line = in_file.readline()
    line = line.strip()
    line = line.split()
    b_x = float(line[0])
    b_y = float(line[1])
    B = Point(b_x, b_y)
    
    # print the string representation of the line AB
    AB = Line(A.x,A.y,B.x,B.y)
    print("Line AB:", AB)
    # print if the lines PQ and AB are parallel or not
    if PQ.is_parallel(AB):
        print("PQ is parallel to AB")
    else:
        print("PQ is not parallel to AB")
    # print if the lines PQ and AB (or extensions) are perpendicular or not
    if PQ.is_perpendicular(AB):
        print("PQ is perpendicular to AB")
        print("Intersection point of PQ and AB:", PQ.intersection_point(AB))
    else:
        print("PQ is not perpendicular to AB")
    # print coordinates of the intersection point of PQ and AB if not parallel
    
    # read the coordinates of the fifth Point G
    line = in_file.readline()
    line = line.strip()
    line = line.split()
    g_x = float(line[0])
    g_y = float(line[1])
    G = Point(g_x, g_y)
    
    # read the coordinates of the sixth Point H
    line = in_file.readline()
    line = line.strip()
    line = line.split()
    h_x = float(line[0])
    h_y = float(line[1])
    H = Point(h_x, h_y)
    GH = Line(G.x,G.y,H.x,H.y)

    # print if the the points G and H are on the same side of PQ
    if PQ.on_same_side(G, H):
        print("G and H are on the same side of PQ")
    else:
        print("G and H are not on the same side of PQ")
    # print if the the points G and H are on the same side of AB
    if AB.on_same_side(G, H):
        print("G and H are on the same side of AB")
    else:
        print("G and H are not on the same side of AB")
    
    '''
    X = Point(0, 1)
    Y = Point(-1, 0)
    
    U = Point(-1, 0)
    V = Point(0, -1)
    
    XY = Line(X.x,X.y,Y.x,Y.y)
    UV = Line(U.x,U.y,V.x,V.y)
    print(XY.is_on_line(Y))
    '''
    #print(XY.is_parallel_y())
    
    # close file "geom.txt"
    in_file.close()
    
if __name__ == "__main__":
    main()

