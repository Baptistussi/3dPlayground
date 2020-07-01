import time

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
