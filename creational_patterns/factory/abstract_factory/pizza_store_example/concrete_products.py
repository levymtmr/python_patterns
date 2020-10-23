from abstract_product import VegPizza


class DeluxeVeggiePizza(VegPizza):

    def prepare(self):
        print('Prepare ', type(self).__name__)


class MexicanVeggiePizza(VegPizza):

    def prepare(self):
        print('Prepare ', type(self).__name__)
