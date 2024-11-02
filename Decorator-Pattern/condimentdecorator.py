from bevarage import Bevarage, BevarageSize
class CondimentsDecorator(Bevarage):
    def __init__(self, bev: Bevarage):
        self.bev = bev

    def getDescription(self):
        pass
    
    def cost(self):
        return self.bev.cost()