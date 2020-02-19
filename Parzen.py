import numpy as np

class Parzen:

    def __init__(self,thc):
        self.taille = thc
        self.xmin = 0
        self.ymin = 0

    def learn(self,xmin,ymin):
        self.xmin = xmin
        self.ymin = ymin


    def predict(self,geomat,grid):
        return