from bevarage import Bevarage

class HouseBlend(Bevarage):
    def __init__(self):
        super().__init__()
        self.setDescription('House Blend')

    def getDescription(self):
        return super().getDescription()
    
    def cost(self):
        return .89
    

class DarkRoast(Bevarage):
    def __init__(self):
        super().__init__()
        self.setDescription('Dark Raost')

    def getDescription(self):
        return super().getDescription()
    
    def cost(self):
        return .99
    
class Decaf(Bevarage):
    def __init__(self):
        super().__init__()
        self.setDescription('Decaf')

    def getDescription(self):
        return super().getDescription()
    
    def cost(self):
        return 1.05

class Espresso(Bevarage):
    def __init__(self):
        super().__init__()
        self.setDescription('Espresso')

    def getDescription(self):
        return super().getDescription()
    
    def cost(self):
        return 1.99