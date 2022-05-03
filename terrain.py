class Terrain:
    def __init__(self, h_w, x_center, y_center):
        self.h_w = h_w
        self.x_center = x_center
        self.y_center = y_center

    def generate_terrain(self):
        """
        Generate a 2D array with a radial gradient
        """
        x = np.linspace(-10, 10, self.h_w)
        y = np.linspace(-10, 10, self.h_w)
        x, y = np.meshgrid(x, y)
        terrain = np.sqrt((x-self.x_center)**2+(y-self.y_center)**2)
        return self.terrain

    def plot_terrain(self):
        """
        Plots in colorbar the 2D array
        """
        plt.imshow(self.terrain)
    
    def calculate_gain(self, x, y):
        """
        Returns the gain for a set of coordinate values"""
        return self.terrain[x][y]