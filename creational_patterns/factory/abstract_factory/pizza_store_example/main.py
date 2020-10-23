from concretes_factories import IndianPizzaFactory, USPizzaFactory


class PizzaStore:

    def __init__(self):
        pass

    def make_pizzas(self):
        for factory in [IndianPizzaFactory, USPizzaFactory]:
            self.factory = factory
            self.NonVegPizza = self.factory.create_non_veg_pizza(self)
            self.VegPizza = self.factory.create_veg_pizza(self)
            self.VegPizza.prepare()
            self.NonVegPizza.server(self.VegPizza)


pizza = PizzaStore()
pizza.make_pizzas()
