from concrete_factory import (
    Nike,
    Adidas,
    Puma
)


class ShoesMultiCompany:

    def __init__(self):
        pass

    def make_shoes(self):
        for factory in [Nike(), Adidas(), Puma()]:
            self.factory = factory
            self.SportShoe = self.factory.create_sport_shoes()
            self.SocialShoe = self.factory.create_social_shoes()
            self.CasualShoe = self.factory.create_casual_shoes()
            self.SportShoe.add_water_protection(self.CasualShoe)
            self.CasualShoe.add_more_confort(self.SocialShoe)
            self.SocialShoe.add_max_layer(self.SportShoe)


shoes = ShoesMultiCompany()
shoes.make_shoes()
