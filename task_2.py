class NotSleeping:
    '''
    Class of people trying to fall asleep
    '''

    def __init__(self, name=None):
        self.name = name
        self.__sheep = 0


    '''
    Number of counted sheep
    '''
    @property
    def sheep(self):
        return self.__sheep

    '''
    Adds one sheep
    '''
    def add_sheep(self):
        self.__sheep += 1

    def __str__(self):
        return f'Засыпающий: {self.name}'

    def __repr__(self):
        return self.__str__()


person = NotSleeping('Вася')
print(person.sheep)
person.add_sheep()
print(person.sheep)
for _ in range(20):
    person.add_sheep()
print(person.sheep)
