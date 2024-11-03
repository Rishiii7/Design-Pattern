from pizza import Pizza

class CheesePizza(Pizza):
    def prepare(self):
        print('Preparing Cheese pizza dough ...')
    
    def bake(self):
        print('Baking the Cheese pizza...')
    
    def cut(self):
        print('Slicing up the Cheese pizza ....')


class VeggiePizza(Pizza):
    def prepare(self):
        print('Preparing Veggie pizza dough ...')
    
    def bake(self):
        print('Baking the Veggie pizza...')
    
    def cut(self):
        print('Slicing up the Veggie pizza ....')

class PepproniPizza(Pizza):
    def prepare(self):
        print('Preparing Pepproni pizza dough ...')
    
    def bake(self):
        print('Baking the Pepproni pizza...')
    
    def cut(self):
        print('Slicing up the Pepproni pizza ....')
