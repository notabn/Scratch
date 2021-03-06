
class Person(object):
    """A representation of a person in 2D Land"""
    def __init__(self,name):
        self.name = name

    def make_noise(self):
        return 'hello'

class DogAdapter(object):
    """Adapts the Dog class through encapsulation"""
    def __init__(self, canine):
        self.canine = canine

    def make_noise(self):
        """This is the only method that's adapted"""
        return self.canine.bark()

    def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        return getattr(self.canine, attr)


class CreatureAdapter(object):
    """Adapts a creature for clients in 2D Land"""
    def __init__(self, creature, make_noise):
        """Pass in the function to use as 'make_noise'"""
        self.creature = creature
        self.make_noise = make_noise
    def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        return getattr(self.creature, attr)

def click_creature(creature):

    return creature.name,creature.make_noise()