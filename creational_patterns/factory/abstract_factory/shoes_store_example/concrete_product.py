from abstract_product import SportShoe


class SoccerNikeShoe(SportShoe):

    def add_water_protection(self, shoes):
        print('Added water protection in a new NIKE soccer shoe',
              type(self).__name__)


class SoccerAdidasShoe(SportShoe):

    def add_water_protection(self, shoes):
        print('Added water protection in a new ADIDAS soccer shoe',
              type(self).__name__)


class SoccerPumaShoe(SportShoe):

    def add_water_protection(self, shoes):
        print('Added water protection in a new PUMA soccer shoe',
              type(self).__name__)
