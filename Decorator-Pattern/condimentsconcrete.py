from condimentdecorator import CondimentsDecorator
from bevarage import Bevarage

class Mocha(CondimentsDecorator):
    def __init__(self, bev: Bevarage):
        super().__init__(bev=bev)
    
    def getDescription(self):
        return self.bev.getDescription() + ', ' + 'Mocha'

    def cost(self):
        return self.bev.cost() + .20

class SteamedMilk(CondimentsDecorator):
    def __init__(self, bev: Bevarage):
        super().__init__(bev=bev)
    
    def getDescription(self):
        return self.bev.getDescription() + ', ' + 'Steamed Milk'

    def cost(self):
        return self.bev.cost() + .10


class Soy(CondimentsDecorator):
    def __init__(self, bev: Bevarage):
        super().__init__(bev=bev)

    def getDescription(self):
        return self.bev.getDescription() + ', ' + 'Soy'


    def cost(self):
        return self.bev.cost() + .15
    
class Whip(CondimentsDecorator):
    def __init__(self, bev: Bevarage):
        super().__init__(bev=bev)
    
    def getDescription(self):
        return self.bev.getDescription() + ', ' + 'Whip'

    def cost(self):
        return self.bev.cost() + .10