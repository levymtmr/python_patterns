from abc import ABC, abstractmethod


class ShoesFactory(ABC):

    @abstractmethod
    def create_social_shoes(self):
        pass
    
    @abstractmethod
    def create_sport_shoes(self):
        pass
    
    @abstractmethod
    def create_casual_shoes(self):
        pass
