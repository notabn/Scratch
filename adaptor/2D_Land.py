from adaptor.dog import Dog
from adaptor.listening import Person,DogAdapter


def animate_objects():
    person = Person('Bob')
    canine = DogAdapter(Dog('Fido'))

    for creature in (person,canine):
        print (creature.name, ' says ' ,creature.make_noise())


if __name__=='__main__':
    animate_objects()

