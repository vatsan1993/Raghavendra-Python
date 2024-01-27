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
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def __str__(self):
        return f'Name: {self._name}, age: {self._age}'

    def __repr__(self):
        return f'Name: {self._name}, age: {self._age}'


scores1 = Score(64,75,34)
scores2 = Score(95,64,43)
scores3 = Score(87, 64,53)

s1 = Student("Max", 20)
s2 = Student("James", 20)
s3 = Student("Blake", 20 )

data = {s1 : scores1, s2 : scores2, s3 : scores3}

# s1, s2 and s3 are not normal keys. they are objects, sorted does not know how to sort them.
# we need to provide the custom sorting using the lambda function
# sorting
# item contains both student object and the score object . it will be in a tuple we need to use 0 or 1
print('sorting by name of the student')
sorted_data_by_name = sorted(data.items(), key = lambda item: (item[0]).get_name())
for student, score in sorted_data_by_name:
    print(student, score)


# sorting based on average marks
print('\nSorting by average')
sorted_data_by_avg = sorted(data.items(), key = lambda item : (item[1]).get_average())
for student, score in sorted_data_by_avg:
    print(student, score)