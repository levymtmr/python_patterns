from abc import ABCMeta, abstractmethod


class VegPizza(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self, veg_pizza):
        pass 
