# This pattern assumes that you have multiple product families in separate class hierarchies (Chair/Sofa).
# Products of the same family must have a common interface.

# All product families have the same variations (Modern/Victorian).

class Chair:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        raise NotImplementedError("Method is not implemented!")

    def sit_on(self):
        raise NotImplementedError("Method is not implemented!")


class ModernChair(Chair):
    def get_color(self):
        print('This modern style chair is %s.' % self._color)

    def sit_on(self):
        print('Now you are sitting on a %s modern style chair' % self._color)


class VictorianChair(Chair):
    def get_color(self):
        print('This victorian style chair is %s.' % self._color)

    def sit_on(self):
        print('Now you are sitting on a %s victorian style chair' % self._color)


class Sofa:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        raise NotImplementedError("Method is not implemented!")

    def sit_on(self):
        raise NotImplementedError("Method is not implemented!")


class ModernSofa(Chair):
    def get_color(self):
        print('This modern style sofa is %s.' % self._color)

    def sit_on(self):
        print('Now you are sitting on a %s modern sofa chair.' % self._color)


class VictorianSofa(Chair):
    def get_color(self):
        print('This victorian style sofa is %s.' % self._color)

    def sit_on(self):
        print('Now you are sitting on a %s victorian style sofa.' % self._color)


# The abstract factory knows about all (abstract) product types.
class Furniture:
    def create_chair(self, color):
        raise NotImplementedError("Method is not implemented!")

    def create_sofa(self, color):
        raise NotImplementedError("Method is not implemented!")


# Each specific factory knows and creates only products of its variation.
class ModernFurniture(Furniture):
    def create_chair(self, color):
        return ModernChair(color)

    def create_sofa(self, color):
        return ModernSofa(color)


class VictorianFurniture(Furniture):
    def create_chair(self, color):
        return VictorianChair(color)

    def create_sofa(self, color):
        return VictorianSofa(color)


# Depending on the configuration (or other conditions), select the desired factory.
if __name__ == '__main__':
    config_furniture_style = 'modern'  # 'modern' or 'victorian'

    if config_furniture_style == 'modern':
        furniture = ModernFurniture()
        chair = furniture.create_chair('red')
        sofa = furniture.create_sofa('white')

    if config_furniture_style == 'victorian':
        furniture = VictorianFurniture()
        chair = furniture.create_chair('blue')
        sofa = furniture.create_sofa('black')

    chair.get_color()
    chair.sit_on()
    sofa.get_color()
    sofa.sit_on()
