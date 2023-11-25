# student and meetings
# student can attend multiple meeting. or a meeting can have multiple students.
# datetime module has a lot of datetime functions and properties
# more on datetime module: https://docs.python.org/3/library/datetime.html
# datetime function helps to create a date and time object.
# timedelta function helps us to create a time object which can be added to a datatime object.
# from module import function



class Student:
    def __init__(self, student_id, name, age, phone):
        self._student_id = student_id
        self._name = name
        self._age = age
        self._phone = phone

    # getters and setter needs to be written
    def getId(self):
        return self._student_id

    def getPhone(self):
        return self._phone

    def getName(self):
        return self._name

    def __str__(self):
        return f"Student id= {self._student_id} name= {self._name} age= {self._age}"

    def __repr__(self):
        return f"Student id= {self._student_id} name= {self._name} age= {self._age}"
