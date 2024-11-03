from pizzaconcrete import CheesePizza, VeggiePizza, PepproniPizza

class PizzaFactory:
    def createPizza(self, type: str):
        pizza = None
        if type == 'Cheese':
            pizza = CheesePizza()
        elif type == 'Veggie':
            pizza = VeggiePizza()
        else:
            pizza = PepproniPizza()
        
        return pizza 

