from bevarage import Bevarage, BevarageSize

class HouseBlend(Bevarage):
    def __init__(self, size: BevarageSize):
        super().__init__(size)
        self.setDescription('House Blend')

    def getDescription(self):
        return super().getDescription()
    
    def cost(self):
        return super().cost() + .89
    

class DarkRoast(Bevarage):
    def __init__(self, size: BevarageSize):
        super().__init__(size)
        self.setDescription('Dark Raost')

    def getDescription(self):
        return super().getDescription()
    
    def cost(self):
        return super().cost() + .99
    
class Decaf(Bevarage):
    def __init__(self, size: BevarageSize):
        super().__init__(size)
        self.setDescription('Decaf')

    def getDescription(self):
        return super().getDescription()
    
    def cost(self):
        return super().cost() + 1.05

class Espresso(Bevarage):
    def __init__(self, size: BevarageSize):
        super().__init__(size)
        self.setDescription('Espresso')

    def getDescription(self):
        return super().getDescription()
    
    def cost(self):
        return super().cost() + 1.99