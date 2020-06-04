#!/usr/bin/python

import pygame
import sys
from pygame.locals import *
import controller

pygame.init()

class Game:
    def __init__(self):
        self.windowSize = (850,550)
        self.freq = 20
        self.scale = 10
        self.control=controller.Controller()
        self.clock=controller.Ticker(self.freq)
    def setup(self):
        self.WINDOW = pygame.display.set_mode(self.windowSize) 
        self.CAPTION = pygame.display.set_caption('3D Playground')
        self.SCREEN = pygame.display.get_surface()
        print "Display Initialized"
        pygame.display.update()
    def drawDots(self):
        self.SCREEN.fill((0,0,0))
        dots = self.control.getDots()
        for dot in dots: pygame.draw.circle(self.SCREEN, (255, 255, 255), dot, 3)
    def loopGame(self):
        print "Starting Main Loop"
        while True:
            pos = pygame.mouse.get_pos()
            # Event Detection
            for event in pygame.event.get():
                if event.type == QUIT: 
                    pygame.quit()
                    sys.exit()
                elif event.type ==  MOUSEBUTTONDOWN:
                    self.control.addDot(pos)
                    #print self.control.getDots()
                elif event.type == KEYDOWN:
                    keys=pygame.key.get_pressed()
                    if keys[K_UP]:
                        self.control.move((0,-1))
                    elif keys[K_DOWN]:
                        self.control.move((0,1))
                    elif keys[K_RIGHT]:
                        self.control.move((1,0))
                    elif keys[K_LEFT]:
                        self.control.move((-1,0))
                    elif keys[K_q]:
                        self.control.turn(1)
                    elif keys[K_e]:
                        self.control.turn(-1)
                    elif keys[K_SPACE]:
                        self.control.reset()
            if self.clock.hasTicd():
                self.drawDots()
                pygame.display.update()

def main():
    game=Game()
    game.setup()
    game.loopGame()

if __name__ == "__main__":
    main()
