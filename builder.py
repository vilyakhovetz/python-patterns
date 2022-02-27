# A builder can create different products using the same building process.
class House:
    pass


# The builder interface declares all possible product configuration steps.
class HouseBuilder:
    def reset(self):
        raise NotImplementedError("Method is not implemented!")

    def build_walls(self):
        raise NotImplementedError("Method is not implemented!")

    def build_doors(self):
        raise NotImplementedError("Method is not implemented!")

    def build_roof(self):
        raise NotImplementedError("Method is not implemented!")


# All concrete builders implement the common interface in their own way.
class WoodenHouseBuilder(HouseBuilder):
    def __init__(self):
        self._house = House()

    def reset(self):
        self._house = House()

    def build_walls(self):
        self._house.walls = 'wooden walls'

    def build_doors(self):
        self._house.doors = 'wooden doors'

    def build_roof(self):
        self._house.roof = 'wooden roof'

    def get_result(self):
        return self._house


class StoneHouseBuilder(HouseBuilder):
    def __init__(self):
        self._house = House()

    def reset(self):
        self._house = House()

    def build_walls(self):
        self._house.walls = 'stone walls'

    def build_doors(self):
        self._house.doors = 'stone doors'

    def build_roof(self):
        self._house.roof = 'stone roof'

    def get_result(self):
        return self._house


# The director knows in what sequence to make the builder work. It works with it through a common builder interface.
# Because of this, he may not know what specific product is being built.
class Director:
    def __init__(self, builder):
        self._builder = builder

    def build_house_without_doors(self):
        self._builder.reset()
        self._builder.build_walls()
        self._builder.build_roof()
        return self._builder.get_result()

    def build_house_without_roof(self):
        self._builder.reset()
        self._builder.build_walls()
        self._builder.build_doors()
        return self._builder.get_result()


# The director receives a specific builder object from the client (application). The application itself knows which
# builder to use in order to get the desired product.

# The finished product is returned by the builder, since the director most often does not know and does not depend on
# specific classes of builders and products.
if __name__ == '__main__':
    builder1 = StoneHouseBuilder()
    director1 = Director(builder1)
    stone_house = director1.build_house_without_roof()
    print('This house has %s, %s' % (stone_house.walls, stone_house.doors))

    builder2 = WoodenHouseBuilder()
    director2 = Director(builder2)
    wooden_house = director2.build_house_without_doors()
    print('This house has %s, %s' % (wooden_house.walls, wooden_house.roof))
