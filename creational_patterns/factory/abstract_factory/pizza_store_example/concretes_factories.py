from abstract_factory import PizzaFactory
from concrete_products import DeluxeVeggiePizza, MexicanVeggiePizza
from another_concrete_product import ChickenPizza, HamPizza


class IndianPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return DeluxeVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza() 


class USPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return MexicanVeggiePizza()

    def create_non_veg_pizza(self):
        return HamPizza()