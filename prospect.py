class Prospect_random():
    
    def __init__(self, terrain, threshold = 0.8):
        self.terrain = terrain
        self.threshold = threshold
        self.x = random.randint(0,len(terrain) - 1)
        self.y = random.randint(0,len(terrain[0] - 1))
        self.gain = terrain[self.x][self.y]
        self.hist = [(self.x, self.y, self.gain)]
        
    def next_pick(self):
        while self.gain <= self.threshold :
            self.random_pick()
        


    def little_step(self):
        self.x += 1
        self.gain = terain[]
        self.y += 0

    
    def random_pick(self):
        x = random.randint(0,len(self.terrain) - 1)
        y = random.randint(0,len(self.terrain[0] - 1))
        gain = terrain[x][y]
        self.hist.append((x,y,gain))
    

        return (x,y,gain)
    
    def gain_calcul(self):
        return terrain[self.x][self.y]

    # def check_position(self)
    