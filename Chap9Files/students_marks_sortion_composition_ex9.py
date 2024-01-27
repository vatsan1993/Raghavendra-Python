# does not use composition
# showing dictionary sorting
class Score:
    def __init__(self, math, science, english):
        self._math = math
        self._science = science
        self._english = english

    def get_math(self):
        return self._math

    def get_science(self):
        return self._science

    def get_english(self):
        return self._english

    def get_average(self):
        return (self._math + self._science + self._english)/3

    def __str__(self):
        return f'Math: {self._math}, Science: {self._science}, English: {self._english}, Avg: {self.get_average()}'

    def __repr__(self):
        return f'Math: {self._math}, Science: {self._science}, English: {self._english}, Avg: {self.get_average()}'


class Student:
    def __init__(self, name, age, scores):
        self._name = name
        self._age = age
        self._scores = scores

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_math(self):
        return self._scores.get_math()

    def get_science(self):
        return self._scores.get_science()

    def get_english(self):
        return self._scores.get_english()

    def get_average(self):
        return self._scores.get_average()

    def __str__(self):
        return f'Name: {self._name}, age: {self._age}, \n\tScores: {self._scores}\n'

    def __repr__(self):
        return f'Name: {self._name}, age: {self._age}, Avg: {self._scores.get_average()}'


scores1 = Score(64,75,34)
scores2 = Score(95,64,43)
scores3 = Score(87, 64,53)

s1 = Student("Max", 20, scores1)
s2 = Student("James", 20, scores2)
s3 = Student("Blake", 20 , scores3)

data = [s1, s2, s3]

# s1, s2 and s3 are not normal values in the list. they are objects, so we have to provide custom sorting using lambda

# x is a student class object
print('sorting by name of the student')
sorted_data_by_name = sorted(data , key = lambda x : x.get_name())
for student in sorted_data_by_name:
    print(student)


# sorting based on average marks
print('\nSorting by average')
sorted_data_by_avg = sorted(data, key = lambda x : x.get_average())
for student in sorted_data_by_avg:
    print(student)