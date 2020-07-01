import numpy as np
import math

import Tools

class Point:
    def __init__(self, coor):
        self.set_rect_coor(coor)
    
    def __getitem__(self, i):
        return self.rcoor[i]
    
    def __repr__(self):
        return str(self.rcoor)
    
    def set_rect_coor(self, rcoor):
        self.rcoor=np.array(rcoor)
    
    def set_2d_coor(self, coor2):
        self.coor2=coor2
    
    def rotate(self, angles):
        self.rcoor=Tools.rotate(self.rcoor, angles)
    
    def move(self, step):
        self.rcoor+=step

class PointCollection:
    pts=[]
    
    def grow(self, otherPts):
        self.pts+=otherPts
    
    def read_point(self):
        x,y,z=input()
        self.pts.append(Point((x,y,z)))
    
    def read_points(self, n=0):
        if n==0: n=input("How many points? ")
        for i in range(n):
            self.read_point()
        print "Done."
    
    def import_points(self, points):
        for point in points:
            self.pts.append(Point(point))
    
    def get_points(self):
        return self.pts
    
    def move(self, step):
        for pt in self.pts:
            pt.move(step)
    
    def rotate(self, angles):
        axis=self.calculate_center()
        self.move(-axis)
        for pt in self.pts:
            pt.rotate(angles)
        self.move(axis)
    
    def calculate_center(self):
        xs = [pt[0] for pt in self.pts]
        ys = [pt[1] for pt in self.pts]
        zs = [pt[2] for pt in self.pts]
        xc = (max(xs)+min(xs))/2.
        yc = (max(ys)+min(ys))/2.
        zc = (max(zs)+min(zs))/2
        self.center=np.array((xc,yc,zc))
        return self.center

class Line:
    def __init__(self, pt1, pt2):
        self.pt1=pt1
        self.pt2=pt2
    
    def get_points(self):
        return (pt1,pt2)

class Polygon(PointCollection):
    lines=[]
    
    def connect_points(self, pt1, pt2):
        self.lines.append( Line(pt1,pt2) )
    
    def get_lines(self):
        return self.lines

class Cube:
    pass

class Sphere:
    pass
