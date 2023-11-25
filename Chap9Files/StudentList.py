class AllStudents:
    def __init__(self):
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def delete_student(self, student_id):
        for i in range(len(self._students)):
            student = self._students[i]
            if student.getId() == student_id:
                self._students.pop(i)
            return student
        return None

    def search(self, student_id):
        for student in self._students:
            if student.getId() == student_id:
                return student
        return None
    def search_by_name(self, name):
        for student in self._students:
            if student.getName().lower() == name.lower():
                return student
        return None
    def search_by_phone(self, phone):
        for student in self._students:
            if student.getPhone() == phone:
                return student
        return None
    def get_students(self):
        return self._students