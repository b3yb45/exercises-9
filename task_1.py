class Dog:
    '''
    Class of dogs
    '''

    def __init__(self, name=None):
        self.name = name

    def say(self):
        return f'{self.name}: Гав!'

    def __str__(self):
        return f'Собака: {self.name}'

    def __repr__(self):
        return self.__str__()


dog = Dog('Шарик')
print(dog.say())
print(dog)
