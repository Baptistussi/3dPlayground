import math
import numpy as np

import Tools

class Camera:
    def __init__(self, pos, sight, screen_size=(850,550), zoom_angle=85):
        self.pos=pos# use np array
        self.sight=sight# use np array
        self.screen_size=screen_size
        self.zoom_angle=zoom_angle
        self.calculate_focus()
    
    def calculate_focus(self):
        self.focus=max(self.screen_size)/math.atan( math.radians(self.zoom_angle) )
        
    def move(self, step):
        self.pos+=step
        print "pos: ",self.pos
    
    def turn(self, angles):
        self.sight+=angles
        print "sight: ",self.sight
    
    def resize_screen(self, screen_size):
        self.screen_size=screen_size
        self.calculate_focus()
    
    def change_zoom(self, increment):
        self.zoom_angle+=increment
        print "zoom: ",self.zoom_angle
        self.calculate_focus()
    
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

