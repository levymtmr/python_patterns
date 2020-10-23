from another_abstract_product import NonVegPizza


class ChickenPizza(NonVegPizza):

    def server(self, veg_pizza):
        print(type(self).__name__, ' is served with Chicken on ',
              type(veg_pizza).__name__)


class HamPizza(NonVegPizza):

    def server(self, veg_pizza):
        print(type(self).__name__, ' is served with Ham on ',
              type(veg_pizza).__name__)
