class Terrain:
    def __init__(self, h_w, p):
        self.h_w = h_w
        self.p = p

    def generate_terrain(self, x_center, y_center):
        """
        Generate a 2D array with a radial gradient
        """
        x = np.linspace(-10, 10, self.h_w)
        y = np.linspace(-10, 10, self.h_w)
        x, y = np.meshgrid(x, y)
        terrain = np.sqrt((x-x_center)**2+(y-y_center)**2)
        return self.terrain
    
    def calculate_gain(self, x, y):
        """
        Returns the gain for a set of coordinate values"""
        return self.terrain[x][y] * bernoulli.rvs(self.p, size=1)