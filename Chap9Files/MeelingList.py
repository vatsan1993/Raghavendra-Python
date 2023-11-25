class AllMeetings:
    def __init__(self):
        self._meetings = []

    def add_meeting(self, meeting):
        self._meetings.append(meeting)

    def add_student_to_meeting(self, meeting_id, student):
        meeting = self.search(meeting_id)
        if meeting != None:
            meeting.add_student(student)

    def remove_meeting(self, meeting_id):
        for meeting in self._meetings:
            if meeting.getId() == meeting_id:
                self._meetings.pop(meeting_id)
                return meeting
        return None

    def remove_student_from_meeting(self, meeting_id, student_id):
        meeting = self.search(meeting_id)
        if meeting != None:
            student_removed = meeting.remove_student_from_meeting(student_id)
            return student_removed
        else:
            return None

    def remove_student(self, student_id):
        for meeting in self._meetings:
            meeting.remove_student_from_meeting(student_id)

    def search(self, meeting_id):
        for meeting in self._meetings:
            if meeting.getId() == meeting_id:
                return meeting
        return None

    def search_by_keyword(self, keyword):
        data = []
        for meeting in self._meetings:
            if meeting.matching_keyword(keyword):
                data.append(meeting)
        return data

    def get_all_meetings_by_id(self):
        return sorted(self._meetings, key=lambda x: x.getId())

    def get_all_meetings_by_name(self):
        return sorted(self._meetings, key=lambda x: x.get_name())

    def get_all_meetings_by_price(self):
        return sorted(self._meetings, key=lambda x: x.get_price())

    def get_students_for_meeting(self, meeting_id):
        meeting = self.search(meeting_id)
        if meeting != None:
            return meeting.get_students()
        else:
            return None

    def get_all_meetings_for_student(self, student_id):
        matched_meetings = []
        for meeting in self._meetings:
            student = meeting.search_student_in_meeting_by_id(student_id)
            if student != None:
                matched_meetings.append(meeting)
        return matched_meetings

    def remove_meeting(self, meeting_id):
        for i in range(len(self._meetings)):
            if self._meetings[i].getId() == meeting_id:
                self._meetings.pop(i)
                return True
        else:
            return False
