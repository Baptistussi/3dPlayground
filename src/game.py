#!/usr/bin/python

import pygame
import sys
import numpy as np
from pygame.locals import *

import Ticker
import Camera
import Tools

pygame.init()

class Game:
    def __init__(self):
        # settings
        self.windowSize = (850,550)
        self.freq = 20
        self.scale = 10
        
        # set tools
        self.clock=Ticker.Ticker(self.freq)
        self.dots=Tools.PointCollection()
        self.set_camera()
        self.set_controls()
    
    def set_controls(self):
        i = np.array((1,0,0))*self.scale
        j = np.array((0,1,0))*self.scale
        k = np.array((0,0,1))*self.scale
        self.controls = {
    K_LEFTBRACKET: [self.cam.move, k ],
    K_RIGHTBRACKET: [self.cam.move, -k ],
    K_z: [self.cam.change_zoom, -5],
    K_x: [self.cam.change_zoom, 5],
    K_UP: [self.cam.move, j ],
    K_DOWN: [self.cam.move, -j ],
    K_RIGHT: [self.cam.move, i ],
    K_LEFT: [self.cam.move, -i ],
    K_SPACE: [self.dots.read_points, 0],
    K_w: [self.cam.turn , -k ], # roll
    K_s: [self.cam.turn , k  ], # roll
    K_a: [self.cam.turn , j  ], # pitch
    K_d: [self.cam.turn , -j ], # pitch
    K_q: [self.cam.turn , i  ], # yaw
    K_e: [self.cam.turn , -i ], # yaw
}
        # controls[key][0]( controls[key][1] )
    
    def set_camera(self):
        pos=np.array((0,0,0))
        s=np.array((0,0,0))
        z=85
        self.cam=Camera.Camera(pos,s,self.windowSize,z)
    
    def setup(self):
        self.WINDOW = pygame.display.set_mode(self.windowSize) 
        self.CAPTION = pygame.display.set_caption('3D Playground')
        self.SCREEN = pygame.display.get_surface()
        print "Display Initialized"
        pygame.display.update()
    
    def draw_dots(self):
        pts = self.cam.display( self.dots.get_points() )
        if pts!=[]:
            for pt in pts: pygame.draw.circle(self.SCREEN, (255, 255, 255), pt, 3)
    
    def draw_lines(self):
        pass
    
    def loopGame(self):
        print "Starting Main Loop"
        while True:
            #pos = pygame.mouse.get_pos()
            # Event Detection
            for event in pygame.event.get():
                if event.type == QUIT: 
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    keys=pygame.key.get_pressed()
                    for i in range(len(keys)):
                        if keys[i]:
                            try:
                                self.controls[i][0]( self.controls[i][1] )
                            except:
                                pass
            if self.clock.hasTicd():
                self.SCREEN.fill((0,0,0))
                self.draw_dots()
                self.draw_lines()
                pygame.display.update()

def main():
    game=Game()
    game.setup()
    
    my_cube=[ (5,5,20), (5,-5,20), (-5,5,20), (-5,-5,20), (5,5,30), (5,-5,30), (-5,5,30), (-5,-5,30) ]
    #my_cube=[ (1,1,15), (1,-1,15), (-1,1,15), (-1,-1,15), (1,1,5), (1,-1,5), (-1,1,5), (-1,-1,5) ]
    game.dots.import_points(my_cube)
    
    game.loopGame()

if __name__ == "__main__":
    main()
