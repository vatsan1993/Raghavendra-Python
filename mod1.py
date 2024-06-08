'''
Documentation for a module mod1

Variables:
a - an integer value 10.

functions
add_values(a,b):
    This function adds the provided values and returns the result


classes:
Person(name, age)
|        This class store details related to a person. It needs name and age of the person.
'''

a = 10

def add_values(a, b):
    '''
    This function returns the sum of a and b.
    :param a: an integer value that we want to perform sum on
    :param b: an integer value that we want to perform sum on
    :return: an  integer value which is the sum of a and b
    '''
    return a + b


class Person:
    '''
    Person class helps Us to store details related to a person.
    '''
    def __init__(self, name, age):
        '''
        This is the constructor for the person class. It helps to create the Person objects
        :param name: name of the person which should be a string
        :param age: age of a person which should be an int value

        Usage: person = Person("Max", 10)
        '''
        self.__name = name
        self.__age = age

    def get_name(self):
        '''
        getter method for the person clas
        :return: returns the name of the person

        :Usage: person.get_name()
        '''
        return self.__name

    def get_age(self):
        '''
        getter method for the age
        :return: returns the age of the person.

        :Usage: person.get_age()
        '''
        return self.__age
