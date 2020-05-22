import time
import tools
import numpy as np

class Ticker:
    def __init__(self, frequency):
        self.T=1./frequency
        self.t0=time.time()
        self.tLast=self.t0
    def setFrequency(self, frequency):
        self.T=1./frequency
    def hasTicd(self):
        now=time.time()
        if now-self.tLast>self.T:
            self.tLast=now
            return True
        else:
            return False

class Controller(tools.Tools):
    def __init__(self):
        self.dots=[]
        self.speed=10
    def addDot(self, pos):
        self.dots.append(pos)
    def getDots(self):
        return self.dots
    def reset(self):
        self.dots=[]
    def move(self, direction):
        mov=np.array(direction)*self.speed
        for i in range(len(self.dots)):
            dot=self.dots[i]
            vet=np.array(dot)
            self.dots[i]=self.slide(vet,mov)
    def turn(self, direction):
        deg=direction
        for i in range(len(self.dots)):
            dot=self.dots[i]
            vet=np.array(dot)
            self.dots[i]=self.array2Pos(self.rotate(vet,deg))
