from Student import Student
from Meeting import  Meeting
from MeelingList import  AllMeetings
from  StudentList import AllStudents
from datetime import datetime, timedelta

class Application:
    def __init__(self):
        self._students = AllStudents()
        self._meetings = AllMeetings()

    def read_data(self):
        meeting_file = 'meetings.csv'
        student_file = 'students_meeting.csv'
        with open(meeting_file) as file:
            for line in file:
                line = line .strip()
                row = line.split(', ')
                meeting_id, name, description, start_time, duration, total_capacity, price = row
                meeting_id = int(meeting_id)
                start_time = datetime.strptime(start_time, '%d/%m/%Y %H:%M')
                duration = int(duration)
                total_capacity = int(total_capacity)
                price = float(price)

                meeting = Meeting(meeting_id, name, description, start_time, duration, total_capacity, price)
                self._meetings.add_meeting(meeting)

        with open(student_file) as file:
            for line in file:
                line = line .strip()
                row = line.split(', ')
                student_id, name, age, phone = row[:4]
                student_id = int(student_id)
                age = int(age)
                meeting_ids = row[4:]
                student = Student(student_id, name, age, phone)
                self._students.add_student(student)
                for meeting_id in meeting_ids:
                    meeting_id = int(meeting_id)
                    self._meetings.add_student_to_meeting(meeting_id, student)

    def get_meeting_sorted_by_id(self):
        meetings = self._meetings.get_all_meetings_by_id()
        for meeting in meetings:
            print(meeting)
    def get_all_meetings_sorted_by_name(self):
        meetings = self._meetings.get_all_meetings_by_name()
        for meeting in meetings:
            print(meeting)
    def get_all_meetings_sorted_by_price(self):
        meetings = self._meetings.get_all_meetings_by_price()
        for meeting in meetings:
            print(meeting)
    def welcome_message(self):
        message = 'Welcome to the event mangement application'
        print(message)
        print('*' * len(message))

    def get_all_students_of_a_meeting(self):
        meeting_id = int(input('Enter meeting id: '))

        students = self._meetings.get_students_for_meeting(meeting_id)
        for student in students:
            print(student)
    def get_all_meetings_a_stundent(self):
        student_id = int(input('Enter student id: '))
        meetings = self._meetings.get_all_meetings_for_student(student_id)
        for meeting in meetings:
            print(meeting)

    def delete_meeting(self):
        meeting_id = int(input('Enter the meeting id to delete: '))
        status = self._meetings.remove_meeting(meeting_id)
        if status:
            print('Meeting deleted successfully')
        else:
            print('Unable to find the meeting')

    def delete_a_student_from_a_meeting(self):
        print('deleting a student from a meeting')
        meeting_id = int(input('Enter the meeting id: '))
        student_id = int(input('Enter student id: '))
        removed_student = self._meetings.remove_student_from_meeting(student_id, meeting_id)
        if not removed_student:
            print('Please check the meeting id or student id')
        else:
            print(f'Removed {removed_student.getName()}')
    def delete_a_student_completely(self):
        print('deleting a student completely')
        student_id = int(input('Enter student id: '))
        removed_student = self._students.delete_student(student_id)
        if removed_student == None:
            print('Student does not exist. ')
        else:
            self._meetings.remove_student(student_id)
            print(f'Removed {removed_student.getName()}')

    def get_students_without_any_meetings(self):
        print('Students without a meeting: ')
        # meetings = self._meetings.get_all_meetings_by_id()
        students = self._students.get_students()
        result = []
        for student in students:
            meetings = self._meetings.get_all_meetings_for_student(student.getId())
            if len(meetings) == 0:
                result.append(student)
        for student in result:
            print(student)
    def search_meeting_by_keyword(self):
        keyword = input('Enter the keyword for search: ')
        meetings = self._meetings.search_by_keyword(keyword)
        for meeting in meetings:
            print(meeting)
    def search_student_by_name(self):
        name = input('Enter the name of the student to search: ')
        student = self._students.search_by_name(name)
        if student:
            print(student)
        else:
            print("Student name not found")
    def search_student_by_phone(self):
        phone = input('Enter phone number: ')
        student = self._students.search_by_phone(phone)
        if student:
            print(student)
        else:
            print('Phone number not found.')
    def print_menu(self):
        print()
        print('Menu')
        print('*****************')
        print(f'''
1. get all meetings  sorted by id
2. get all meetings sorted by name
3. get all meetings sorted by price
4. get all students of a meeting
5. get all meetings a stundent
6. delete a meeting
7. delete a student from a meeting
8. delete a student completely.
9. Get students without any meetings.
10. search meeting by keyword
11. search student by name
12. search student by phone
0. Quit

''')


def main():
    app = Application()
    app.read_data()
    app.welcome_message()
    while True:
        app.print_menu()
        choice = int(input('Enter the menu choice:'))
        if choice == 1:
            app.get_meeting_sorted_by_id()
        elif choice == 2:
            app.get_all_meetings_sorted_by_name()
        elif choice == 3:
            app.get_all_meetings_sorted_by_price()
        elif choice == 4:
            app.get_all_students_of_a_meeting()
        elif choice == 5:
            app.get_all_meetings_a_stundent()
        elif choice ==6:
            app.delete_meeting()
        elif choice == 7:
            app.delete_a_student_from_a_meeting()
        elif choice == 8:
            app.delete_a_student_completely()
        elif choice == 9:
            app.get_students_without_any_meetings()
        elif choice == 10:
            app.search_meeting_by_keyword()
        elif choice == 11:
            app.search_student_by_name()
        elif choice == 12:
            app.search_student_by_phone()
        elif choice == 0:
            print('bye')
            break


main()

# 30/10/2023 09:00