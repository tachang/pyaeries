import unittest
import logging
import pyaeries

from settings import API_HOST, CERTIFICATE_AUTH_TOKEN

log = logging.getLogger(__name__)

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.api = pyaeries.AeriesApi(host = API_HOST, certifcate_auth_token = CERTIFICATE_AUTH_TOKEN)
        self.school_code = 990

    def testGetElementarySchool(self):
        students = self.api.get_students(self.school_code)
        teachers = self.api.get_teachers(self.school_code)

        print "Number of students: %d" % len(students)
        print "Number of teachers: %d" % len(teachers)

        teachers_students = {}

        for teacher in teachers:
            teachers_students[teacher['TeacherNumber']] = []

        for student in students:
            teachers_students[student['TeacherNumber']].append(student)

        for key, value in teachers_students.items():
            print key, map(lambda x: x['StudentNumber'], value)

        terms = self.api.get_school_term(self.school_code)

        print terms