# we use this to convert function to key in sorting.
from functools import cmp_to_key
class Course:
    def __init__(self, c_id, name, subject, level):
        self._id = c_id
        self._name = name
        self._subject = subject
        self._level = level

    def get_id(self):
        return self._id

    def get_level(self):
        return self._level
    def __str__(self):
        return f'Course id: {self._id}, Name: {self._name}, Subject: {self._subject}, Level: {self._level}'

    def __repr__(self):
        return f'{self._id} - {self._name}'


class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._courses = []

    def get_name(self):
        return self._name

    def add_course(self, course):
        self._courses.append(course)

    # this function is used as lambda function
    # we are only comparing the level.
    @staticmethod
    def sort_by_level(course):
        level = course.get_level().lower()
        if level == 'beginner':
            return -1
        if level == 'intermediate':
            return 0
        if level == 'advanced':
            return 1

    @staticmethod
    def sort_by_level_id(course1, course2):
        level1 = course1.get_level().lower()
        level2 = course2.get_level().lower()
        if level1 == level2:
            return course1.get_id() - course2.get_id()
        else:
            if level1 == 'beginner':
                return -1
            elif level2 == 'intermediate':
                return 0
            elif level1 == 'advanced':
                return 1
    def __len__(self):
        return len(self._courses)

    def __str__(self):
        output = f'Student Name: {self._name}, Age: {self._age}'
        # using basic sort as lambda function
        # if two course have same level the will appear in the order which they are added.

        # courses_sorted = sorted(self._courses, key=Student.sort_by_level)

        # we need this technique to sort the levels. then if there is same level, we sort based on the id.
        # using advanced sort like a comparision function which needs to be converted to key
        courses_sorted = sorted(self._courses, key=cmp_to_key(Student.sort_by_level_id))
        for course in courses_sorted:
            output += '\n\t'+ str(course)

        output += '\n'
        return output

c1 = Course(101, 'AP Computer Science', 'python', 'beginner')
c2 = Course(102, 'AP Computer Science 2', 'python', 'intermediate')
c3 = Course(103, 'Data Science Fundamentals', 'python', 'beginner')
c4 = Course(104, 'Python for Data Science', 'python', 'intermediate')
c5 = Course(105, 'Data Science for Professionals', 'python', 'Advanced')
c6 = Course(106, 'Applied Machine Learning', 'python', 'Advanced')


s1 = Student('Max', 20)
s2 = Student('Bill',20)
s3 = Student('James', 21)
s4 = Student('Zack', 22)

s1.add_course(c4)

s1.add_course(c3)
s1.add_course(c1)
s1.add_course(c6)

s2.add_course(c4)
s2.add_course(c1)
s2.add_course(c3)

s3.add_course(c4)
s3.add_course(c1)
s3.add_course(c3)

s4.add_course(c4)
s4.add_course(c5)

# this will only sort the courses for each student
students = [s1, s2, s3, s4]
for student in students:
    print(student)


# sorting students by name
sorted_students = sorted(students, key = lambda student: student.get_name())
print('Sorting By student Names:')
for student in sorted_students:
    print(student)


# sorting students based on number of courses student takes(less to more)
# if same number of courses. we need to sort it by name of the student
# lambda cannot be used. so we use the cmp_to_key()

def sort_num_courses(s1, s2):
    if len(s1) - len(s2) == 0:
        if s1.get_name() < s2.get_name():
            return -1
        elif s1.get_name() == s2.get_name():
            return 0
        else:
            return 1
    elif len(s1) < len(s2):
        return -1
    else:
        return 1

sorted_students = sorted(students, key = cmp_to_key(sort_num_courses) )
print('Sorting By course length:')
for student in sorted_students:
    print(student)

# simpler way
sorted_students = sorted(students, key = lambda student: (len(student),student.get_name()))

print('Sorting By course length Alternative way:')
for student in sorted_students:
    print(student)