from pizzaconcrete import CheesePizza, VeggiePizza, PepproniPizza
from pizzastore import PizzaStore

class NYPizzaFactory(PizzaStore):
    def createPizza(self, type: str):
        pizza = None
        if type == 'Cheese':
            pizza = CheesePizza()
        elif type == 'Veggie':
            pizza = VeggiePizza()
        else:
            pizza = PepproniPizza()
        
        return pizza 

