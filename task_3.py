class NotSleeping:
    '''
    Class of people trying to fall asleep
    '''

    def __init__(self, name=None):
        self.name = name
        self.__sheep = 0

    '''
    Adds one sheep
    '''
    def add_sheep(self):
        self.__sheep += 1

    '''
    Lost track of counted sheep
    '''
    def lost(self):
        self.__sheep = 0

    '''
    Returns the number of counted sheep
    '''
    def get_count_sheep(self):
        return self.__sheep

    def __str__(self):
        return f'Засыпающий: {self.name}'

    def __repr__(self):
        return self.__str__()


person = NotSleeping('Ivan')
print(person.get_count_sheep())
person.add_sheep()
print(person.get_count_sheep())
for i in range(10):
    person.add_sheep()
print(person.get_count_sheep())
person.lost()
print(person.get_count_sheep())
