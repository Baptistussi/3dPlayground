import numpy as np
import math

class Point:
    def __init__(self, coor):
        self.set_rect_coor(coor)
    
    def __getitem__(self, i):
        return self.rcoor[i]
    
    def __repr__(self):
        return str(self.rcoor)
    
    def set_rect_coor(self, rcoor):
        self.rcoor=np.array(rcoor)
    
    def get_spherical_coor(self):
        # source: https://pt.wikipedia.org/wiki/Sistema_esf%C3%A9rico_de_coordenadas
        x,y,z=self.rcoor
        r=math.sqrt(x**2+y**2+z**2)
        if r==0:
            theta=0
            gama=0
        else:
            theta=math.degrees( math.acos(x/math.sqrt(x**2+y**2)) )
            gama=math.degrees( math.acos(z/r) )
        return r, theta, gama
    
    def get_rotated_coor(self, angles):
        # source: https://en.wikipedia.org/wiki/Rotation_matrix
        # rz(alpha), ry(beta), rx(gama) ---> yaw, pitch, roll
        rd_angles=np.radians(angles)
        sin_alpha, sin_beta, sin_gama = np.sin(rd_angles)
        cos_alpha, cos_beta, cos_gama = np.cos(rd_angles)
        R=np.array( [ [cos_alpha*cos_beta, cos_alpha*sin_beta*sin_gama-sin_alpha*cos_gama, cos_alpha*sin_beta*cos_gama+sin_alpha*sin_gama],
                        [sin_alpha*cos_beta, sin_alpha*sin_beta*sin_gama+cos_alpha*cos_gama, sin_alpha*sin_beta*cos_gama-cos_alpha*sin_gama],
                        [-sin_beta, cos_beta*sin_gama, cos_beta*cos_gama] ])
        return R.dot(self.rcoor)
    
    def rotate(self, angles):
        self.rcoor=self.get_rotated_coor(angles)
    
    def get_moved_coor(self, step):
        return self.rcoor+step
    
    def move(self, step):
        self.rcoor=self.get_moved_coor(step)
    
    def is_visible(self, zoom):
    # review. not great yet
        r, theta, gama = self.get_spherical_coor()
        if gama<zoom:
            return True
        else:
            return False

class PointCollection:
    def __init__(self):
        self.pts=[]
    
    def grow(self, otherPts):
        self.pts+=otherPts
    
    def read_point(self):
        x,y,z=input()
        self.pts.append(Point((x,y,z)))
    
    def read_points(self, n=0):
        if n==0: n=input("How many points? ")
        for i in range(n):
            self.read_point()
    
    def get_points(self):
        return self.pts
    
    def move(self, step):
        for pt in self.pts:
            pt.move(step)
    
    def rotate(self, angles):
        for pt in self.pts:
            pt.rotate(step)

class Line:
    def __init__(self, pt1, pt2):
        self.pt1=pt1
        self.pt2=pt2

class 3dObject(PointCollection):
    def __init__(self):
        lines=[]
    
    def connect_points(self, pt1, pt2):
        self.lines.append( Line(pt1,pt2) )

class Cube:
    pass

class Sphere:
    pass
