# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from terrain import *
from prospect import *
from vizualizer import *
import pandas as pd


terrain = Terrain(9, 0.3, -5, 5)
greedy = Prospect_greedy(terrain)

for i in range(1000):

    greedy.next_pick()

print(greedy.hist)
print(greedy.esp)
plt.plot(np.cumsum(greedy.ruby_hist))
plt.grid()
plt.show()

