from another_abstract_product_2 import CasualShoe


class ClassicNikeShoe(CasualShoe):

    def add_more_confort(self, shoes):
        print(type(self).__name__,
              'Added a new max layer to shine your Nike shoes ',
              type(shoes).__name__)


class ClassicAdidasShoe(CasualShoe):

    def add_more_confort(self, shoes):
        print(type(self).__name__,
              'Added a new max layer to shine your Adidas shoes ',
              type(shoes).__name__)


class ClassicPumaShoe(CasualShoe):

    def add_more_confort(self, shoes):
        print(type(self).__name__,
              'Added a new max layer to shine your Puma shoes ',
              type(shoes).__name__)
