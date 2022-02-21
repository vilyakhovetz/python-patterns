# The Factory Method pattern is applicable when there is a hierarchy of Product classes.

# Basic product
class Transport:
    def __init__(self, cargo):
        self._cargo = cargo

    def get_cargo(self):
        raise NotImplementedError("Method is not implemented!")

    def deliver(self):
        raise NotImplementedError("Method is not implemented!")


# Product A
class Truck(Transport):
    def get_cargo(self):
        print('%s travel on land' % self._cargo)

    def deliver(self):
        print('Truck delivered %s' % self._cargo)


# Product B
class Ship(Transport):
    def get_cargo(self):
        print('%s travel by sea' % self._cargo)

    def deliver(self):
        print('Ship delivered %s' % self._cargo)


# The base class of the factory. Note that "factory" is just an additional role for the class. It already has some
# kind of business logic that requires the creation of a variety of products.
class Logistics:
    def plan_delivery(self, cargo):
        print('...some operations')
        transport = self.create_transport(cargo)
        transport.get_cargo()
        print('...a little bit later')
        transport.deliver()

    # Factory method
    def create_transport(self, cargo):
        raise NotImplementedError("Method is not implemented!")


# Concrete factories override the factory method and return their own products from it.
class TruckLogistics(Logistics):
    def create_transport(self, cargo):
        return Truck(cargo)


class ShipLogistics(Logistics):
    def create_transport(self, cargo):
        return Ship(cargo)


# The application creates a certain factory depending on certain conditions.
if __name__ == '__main__':
    ship = ShipLogistics()
    ship.plan_delivery('Apples')
    print()
    truck = TruckLogistics()
    truck.plan_delivery('Oranges')
