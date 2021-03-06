#!/usr/bin/python

import pygame
import sys
import numpy as np
from pygame.locals import *

import Ticker
import Camera
import Objects

pygame.init()

class Game:
    def __init__(self):
        # settings
        self.windowSize = (850,550)
        self.freq = 20
        self.scale = 10
        #object
        self.dots=Objects.Cube((0.,0.,30.),10.)
        # set tools
        self.clock=Ticker.Ticker(self.freq)
        self.set_camera()
        self.set_controls()
    
    def set_controls(self):
        i = np.array((1,0,0))*self.scale
        j = np.array((0,1,0))*self.scale
        k = np.array((0,0,1))*self.scale
        self.controls = {
                    K_UP: [self.cam.move, k ],
                    K_DOWN: [self.cam.move, -k ],
                    K_z: [self.cam.change_zoom, -5],
                    K_x: [self.cam.change_zoom, 5],
                    K_w: [self.dots.rotate , k ], # roll
                    K_s: [self.dots.rotate , -k  ], # roll
                    K_a: [self.dots.rotate , -j  ], # pitch
                    K_d: [self.dots.rotate , j ], # pitch
                    K_q: [self.dots.rotate , -i  ], # yaw
                    K_e: [self.dots.rotate , i ], # yaw
        }
        # controls[key][0]( controls[key][1] )
    
    def set_camera(self):
        pos=np.array((5,5,0))
        s=np.array((0,0,0))
        z=85
        self.cam=Camera.Camera(pos,s,self.windowSize,z)
    
    def setup(self):
        self.WINDOW = pygame.display.set_mode(self.windowSize) 
        self.CAPTION = pygame.display.set_caption('3D Playground')
        self.SCREEN = pygame.display.get_surface()
        print "Display Initialized"
        pygame.display.update()
    
    def get_projection(self):
        self.points = self.cam.display( self.dots.get_points() )
        self.dots.update_projection(self.points)
        self.lines = self.dots.get_2d_lines()
        
    def draw_points(self):
        if self.points!=[]:
            for pt in self.points:
                if pt: pygame.draw.circle(self.SCREEN, (255, 255, 255), pt, 3)
    
    def draw_lines(self):
        if self.lines!=[]:
            for l in self.lines:
                try:
                    pygame.draw.line(self.SCREEN, (255,255,255), l[0], l[1], 1)
                except:
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
                self.get_projection()
                self.draw_points()
                self.draw_lines()
                pygame.display.update()

def main():
    game=Game()
    game.setup()
    game.loopGame()

if __name__ == "__main__":
    main()
