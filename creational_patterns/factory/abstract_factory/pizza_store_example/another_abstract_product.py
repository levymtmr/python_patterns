from abc import ABCMeta, abstractmethod


class NonVegPizza(metaclass=ABCMeta):

    @abstractmethod
    def server(self, veg_pizza):
        pass