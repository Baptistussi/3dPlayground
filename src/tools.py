import numpy as np

class Tools:
    def rotate(self,vet, deg):  
        theta=np.radians(deg)
        s,c=np.sin(theta),np.cos(theta)
        R=np.array( [ [c,s], [-s,c] ] )
        return R.dot(vet)
    def slide(self,vet, mov):
        return vet+mov
    def array2Pos(self,arr):
        arrl=[int(round(x)) for x in arr.tolist()]
        return tuple(arrl)
