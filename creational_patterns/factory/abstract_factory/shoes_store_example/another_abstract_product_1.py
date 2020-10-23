from abc import ABC, abstractmethod


class SocialShoe(ABC):

    @abstractmethod
    def add_max_layer(self, shoe):
        pass