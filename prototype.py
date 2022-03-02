# Basic prototype
class Shape:
    # Copying of all fields of the object occurs in the constructor.
    def __init__(self, x=None, y=None, color=None, source=None):
        if source is not None:
            self.x = source.x
            self.y = source.y
            self.color = source.color
        else:
            self.x = x
            self.y = y
            self.color = color

    # The result of a clone operation will always be an object from the Shape class hierarchy.
    def clone(self):
        raise NotImplementedError("Method is not implemented!")


# Specific prototype. The clone method creates a new object and passes its own object to its constructor for copying.
# By this we are trying to get the atomicity of the clone operation. In this implementation, until the constructor is
# executed, the new object does not yet exist. But as soon as the constructor is completed, we get a completely
# finished clone object, and not an empty object that needs to be filled.
class Rectangle(Shape):
    def __init__(self, x=None, y=None, color=None, width=None, height=None, source=None):
        super().__init__(x=x, y=y, color=color, source=source)
        if source is not None:
            self.width = source.width
            self.height = source.height
        else:
            self.width = width
            self.height = height

    def clone(self):
        return Rectangle(source=self)


class Circle(Shape):

    def __init__(self, x=None, y=None, color=None, radius=None, source=None):
        # The call to the parent constructor is needed to copy potential private fields declared in the parent class.
        super().__init__(x=x, y=y, color=color, source=source)
        if source is not None:
            self.radius = source.radius
        else:
            self.radius = radius

    def clone(self):
        return Circle(source=self)


if __name__ == '__main__':
    shapes = []
    circle1 = Circle(x=1, y=5, color='red', radius=7)
    shapes.append(circle1)
    circle2 = circle1.clone()
    shapes.append(circle2)
    rectangle1 = Rectangle(x=5, y=3, color='yellow', width=20, height=30)
    shapes.append(rectangle1)

    # An unobvious advantage of the Prototype is that you can clone a set of objects without knowing their concrete
    # classes.
    shares_copy = []
    for shape in shapes:
        shares_copy.append(shape.clone())

    # For example, we don't know what specific objects are inside the shapes array. But thanks to polymorphism,
    # we can blindly clone all objects. The "clone" method of the class that this object is will be executed.
    print(shares_copy)

    # The shapes_copy variable will contain exact copies of the elements of the shapes array.
