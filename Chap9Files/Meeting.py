from datetime import datetime, timedelta
class Meeting:
    def __init__(self, meeting_id, name, description, start_time, duration, total_capacity=100, price=20):
        self._meeting_id = meeting_id
        self._name = name
        self._description = description
        self._start_time = start_time
        self._duration = duration
        self._end_time = start_time + timedelta(minutes=duration)
        self._total_capacity = total_capacity
        self._available_tickets = total_capacity
        self._price = price
        self._students = []

    def getId(self):
        return self._meeting_id

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def __str__(self):
        return f'''Meeting_id: {self._meeting_id} 
        Name:{self._name}
        Description: {self._description}
        Start time: {self._start_time}
        End time: {self._end_time}
        Duration: {self._duration}
        Available Tickets: {self._available_tickets}
        Price: ${self._price}'''

    def __repr__(self):
        return f'''Meeting_id: {self._meeting_id} 
        Name:{self._name}
        Description: {self._description}
        Start time: {self._start_time}
        End time: {self._end_time}
        Duration: {self._duration}
        Available Tickets: {self._available_tickets}
        Price: ${self._price}'''

    def add_student(self, student):
        self._students.append(student)
        self._available_tickets -= 1

    def remove_student_from_meeting(self, student_id):
        for i in range(len(self._students)):
            student = self._students[i]
            if student.getId() == student_id:
                self._students.pop(i)
                self._available_tickets += 1
                return student
        return None

    def search_student_in_meeting_by_id(self, student_id):
        for student in self._students:
            if student.getId() == student_id:
                return student
        return None

    def search_student_in_meeting_by_phone(self, phone):
        for student in self._students:
            if student.getPhone() == phone:
                return student
        return None

    def search_student_in_meeting_by_Name(self, name):
        students = []
        for student in self._students:
            if name in student.getName():
                students.append(student)
        return students

    def matching_keyword(self, keyword):
        keyword = keyword.lower()
        if keyword in self._name.lower() or keyword in self._description.lower():
            return True

    def get_students(self):
        return self._students

