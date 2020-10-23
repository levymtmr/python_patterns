from abstract_factory import ShoesFactory
from concrete_product import (
    SoccerNikeShoe,
    SoccerAdidasShoe,
    SoccerPumaShoe
)
from another_concrete_product_2 import (
    ClassicNikeShoe,
    ClassicAdidasShoe,
    ClassicPumaShoe
)
from another_concrete_product_1 import (
    LetterNikeShoe,
    LetterAdidasShoe,
    LetterPumaShoe
)


class Nike(ShoesFactory):

    def create_sport_shoes(self):
        return SoccerNikeShoe()

    def create_casual_shoes(self):
        return ClassicNikeShoe()

    def create_social_shoes(self):
        return LetterNikeShoe()


class Adidas(ShoesFactory):

    def create_sport_shoes(self):
        return SoccerAdidasShoe()

    def create_casual_shoes(self):
        return ClassicAdidasShoe()

    def create_social_shoes(self):
        return LetterAdidasShoe()


class Puma(ShoesFactory):

    def create_sport_shoes(self):
        return SoccerPumaShoe()

    def create_casual_shoes(self):
        return ClassicPumaShoe()

    def create_social_shoes(self):
        return LetterPumaShoe()
