class Visualizer:

    def __init__(self, terrain, prospect):
        self.terrain = terrain
        self.prospect = prospect
    
    def plot_perf(self, historic):
        """
        Plot a 2D map representing the gain that were found.
        historic : DataFrame with columns x,y,gain for each trial.
        """
        fig, ax = plt.subplots(figsize=(20,4))
        ax.plot(historic, linestyle='', marker='*')
        ax.set_xlabel('nb tentatives')
        ax.set_ylabel('gain (UA)')
        plt.show()
        

    def plot_terrain(self):
        """
        Plots in colorbar the 2D array with discovered gains.
        """
        plt.imshow(self.terrain)
            