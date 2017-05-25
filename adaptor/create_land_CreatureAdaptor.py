from adaptor.dog import Dog
from adaptor.cat import Cat
from adaptor.twoD_Land import Person,CreatureAdapter


def animate_objects():
    person = Person('Bob')
    fido = Dog('Fido')
    canine = CreatureAdapter(fido,fido.bark)
    whiskers = Cat('Whiskers')
    feline = CreatureAdapter(whiskers,whiskers.meow)

    for creature in (person,canine,feline):
        print (creature.name, ' says ' ,creature.make_noise())


if __name__=='__main__':
    animate_objects()