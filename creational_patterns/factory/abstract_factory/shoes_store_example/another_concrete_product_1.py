from another_abstract_product_1 import SocialShoe


class LetterNikeShoe(SocialShoe):

    def add_max_layer(self, shoes):
        print(type(self).__name__,
              'Added a new max layer to shine your Nike shoes ',
              type(shoes).__name__)


class LetterAdidasShoe(SocialShoe):

    def add_max_layer(self, shoes):
        print(type(self).__name__,
              'Added a new max layer to shine your Adidas shoes ',
              type(shoes).__name__)


class LetterPumaShoe(SocialShoe):

    def add_max_layer(self, shoes):
        print(type(self).__name__,
              'Added a new max layer to shine your Puma shoes ',
              type(shoes).__name__)
