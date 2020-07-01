import numpy as np
import math

# 3d points tools

def rotate(coor, angles):
    # source: https://en.wikipedia.org/wiki/Rotation_matrix
    # rz(alpha), ry(beta), rx(gama) ---> yaw, pitch, roll
    rd_angles=np.radians(angles)
    sin_alpha, sin_beta, sin_gama = np.sin(rd_angles)
    cos_alpha, cos_beta, cos_gama = np.cos(rd_angles)
    R=np.array( [ [cos_alpha*cos_beta, cos_alpha*sin_beta*sin_gama-sin_alpha*cos_gama, cos_alpha*sin_beta*cos_gama+sin_alpha*sin_gama],
                    [sin_alpha*cos_beta, sin_alpha*sin_beta*sin_gama+cos_alpha*cos_gama, sin_alpha*sin_beta*cos_gama-cos_alpha*sin_gama],
                    [-sin_beta, cos_beta*sin_gama, cos_beta*cos_gama] ])
    return R.dot(coor)

def cart2spherical(cart):
    # source: https://pt.wikipedia.org/wiki/Sistema_esf%C3%A9rico_de_coordenadas
    x,y,z=cart
    r=math.sqrt(x**2+y**2+z**2)
    if r==0:
        theta=0
        gama=0
    else:
        theta=math.degrees( math.acos(x/math.sqrt(x**2+y**2)) )
        gama=math.degrees( math.acos(z/r) )
    return (r, theta, gama)

def is_visible(zoom, sph):
# review. not great yet
    r, theta, gama = sph
    if gama<zoom:
        return True
    else:
        return False

# point collection tools



# camera tools

def calculate_focus(screen_size, zoom_angle):
    return max(self.screen_size)/math.atan( math.radians(self.zoom_angle) )

def project(point, cam):
    pass

def display(point, screen_size):
    pass

def rotate_points(self, points):
    rotation_angles=(-self.sight[0], -self.sight[1], -self.sight[2])
    rpoints=[Tools.Point( point.get_rotated_coor(rotation_angles) ) for point in points]
    return rpoints

def move_points(self, points):
    step=-self.pos
    mpoints=[Tools.Point( point.get_moved_coor(step) ) for point in points]
    return mpoints

def get_visible_points(self, points):
    vpoints=[]
    for point in points:
        if point.is_visible(self.zoom_angle):
            vpoints.append(point)
    return vpoints

def project(self, point):
    x,y,z=point
    if z==0: return False
    else:
        xl=self.focus*x/z
        yl=self.focus*y/z
        #print "xl: {}\nyl: {}".format(xl,yl)
        #raw_input()
        return (xl,yl)

def display(self, points):
    vpoints=self.get_visible_points( self.rotate_points( self.move_points(points) ) )
    dpoints=[]
    for point in vpoints:
        dpoint=self.project(point)
        if dpoint!=False:
            x,y=dpoint
            x=int( x + self.screen_size[0]/2 )
            y=int( self.screen_size[1]/2 - y )
            dpoints.append( (x,y) )
    return dpoints

