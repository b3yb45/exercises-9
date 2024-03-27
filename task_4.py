class User:
    '''
    Class of Users
    '''

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        self.__id = id
        self.__nick_name = nick_name
        self.__first_name = first_name
        self.__last_name = last_name
        self.__middle_name = middle_name
        self.__gender = gender

    '''
    Updates one attribute: nick name, first name, last name, middle name or gender
    '''
    def update(self, attr, value):
        if isinstance(attr, str) and isinstance(value, str):
            if attr == 'nick_name':
                self.__nick_name = value
                return

            if attr == 'first_name':
                self.__first_name = value
                return

            if attr == 'last_name':
                self.__last_name = value
                return

            if attr == 'middle_name':
                self.__middle_name = value
                return

            if attr == 'gender':
                self.__gender = value
                return

    def __str__(self):
        return f'User: {self.__id} {self.__nick_name} {self.__first_name} {self.__last_name} {self.__middle_name} ' \
               f'{self.__gender}'

    def __repr__(self):
        return self.__str__()


user = User('1', 'Vanya', 'Ivan')
print(user)
user.update('last_name', 'Ivanov')
print(user)
user.update('middle_name', 'Ivanovich')
user.update('gender', 'male')
print(user)
