"""
This module is a simple example for a module inside a package
we have 4 component here.
1. random_value: 100
2. add_odds: adds all odd value in a list
3. find_value: finds all the indexes of a target value.
4. Student class: creates a student object
"""


random_value = 100

def find_value(lst, target):
    """
    finds all the indexes of a target value.
    :param lst: list
    :param target:  value to find
    :return: all index of a target value.
    """
    indexes = []
    for i in range(len(lst)):
        if lst[i] == target:
            indexes.append(i)

    return indexes


def add_odds(lst):
    """
    adds all odd value in a list
    :param lst: list
    :return: the total
    """
    total = 0

    for val in lst:
        if val % 2 == 1:
            total += val

    return total

class Student:
    """
    Helps to create a student object
    """
    def __init__(self, name, age, score):
        """
        Constructor
        :param name: name of the student
        :param age: age of the student
        :param score: score of the student
        """
        self.__name = name
        self.__age = age
        self.__score = score

    def get_name(self):
        """
        gets the name of the student
        :return:  name of the student
        """
        return self.__name

    def get_age(self):
        """
        gets the age of the student
        :return:  age of the student
        """
        return self.__age

    def get_score(self):
        """
        gets the score of the student
        :return:  score of the student
        """
        return self.__score

