# Imports
import numpy as np
import matplotlib as mlp
from scipy.stats import bernoulli
from terrain import *
from vizualizer import *




class Prospect_greedy():
    
    def __init__(self, terrain, epsilon = 0.1):
        self.terrain = terrain
        self.epsilon = epsilon
        self.xmax = terrain.h_w - 1
        self.ymax = terrain.h_w - 1
        self.x = np.random.randint(0,self.xmax)
        self.y = np.random.randint(0,self.ymax)
        self.hist = [[[]] * self.xmax] * self.ymax
        self.esp = np.zeros((self.xmax, self.ymax))
        self.ruby_hist = []


    def next_pick(self):
        self.d = np.random.random()
        if self.epsilon < self.d :
            self.max_esp()
        else :
            self.uniform()
        self.esp[self.x][self.y] = np.mean(self.hist[self.x][self.y])


        
        

    def uniform(self):
        self.x = np.random.randint(0, self.xmax)
        self.y = np.random.randint(0, self.ymax)
        self.hist[self.x][self.y].append(self.terrain.calculate_gain(self.x, self.y))
        self.ruby_hist.append(self.terrain.calculate_gain(self.x, self.y))


    def max_esp(self):

        result = np.where(self.esp == np.amax(self.esp ))
        self.x = int(result[0][0])
        self.y = int(result[1][0])
        self.hist[self.x][self.y].append(self.terrain.calculate_gain(self.x, self.y))
        self.ruby_hist.append(self.terrain.calculate_gain(self.x, self.y))


