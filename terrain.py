import numpy as np 
from scipy.stats import bernoulli

class Terrain: 

    def __init__(self, h_w, p, x_center, y_center):
        """
        Generate a 2D array with a radial gradient
        """
        self.h_w = h_w
        self.p = p
        x = np.linspace(-10, 10, self.h_w)
        y = np.linspace(-10, 10, self.h_w)
        x, y = np.meshgrid(x, y)
        self.terrain = np.sqrt((x-x_center)**2+(y-y_center)**2)
    
    def calculate_gain(self, x, y):
        """
        Returns the gain for a set of coordinate values"""
        return self.terrain[x][y] * bernoulli.rvs(self.p, size=1)