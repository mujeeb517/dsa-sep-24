# inheritance
# method overriding
# method hiding
# public private

class Animal:
    def __init__(self):
         print('Constructor of Animal')

    def makeSound(self):
        print('making sound')

# parent, super
# child, derived, sub
class Dog(Animal):
    def __init__(self):
         print('Constructor of Dog')

    def makeSound(self):
        print('Bow Bow')

    def printDog(self):
        print('printing..')


class SplDog(Dog):

    def __m1__(self):
        print('private method')

    def __init__(self):
        print('Constructor of Spl.Dog')
    

dg = SplDog()
