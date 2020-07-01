import math
import numpy as np

import Tools

class Camera:
    def __init__(self, pos, sight, screen_size=(850,550), zoom_angle=85):
        self.pos=pos# use np array
        self.sight=sight# use np array
        self.screen_size=screen_size
        self.zoom_angle=zoom_angle
        self.focus=Tools.calculate_focus(screen_size, zoom_angle)
        
    def move(self, step):
        self.pos+=step
        print "pos: ",self.pos
    
    def turn(self, angles):
        self.sight+=angles
        print "sight: ",self.sight
    
    def resize_screen(self, screen_size):
        self.screen_size=screen_size
        self.focus=Tools.calculate_focus(screen_size, zoom_angle)
    
    def change_zoom(self, increment):
        self.zoom_angle+=increment
        print "zoom: ",self.zoom_angle
        self.focus=Tools.calculate_focus(screen_size, zoom_angle)
    #----------------------------------------------------------------------
