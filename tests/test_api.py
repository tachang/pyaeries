import unittest
import logging
import pyaeries


log = logging.getLogger(__name__)


DEMO_CERTIFICATE_AUTH_TOKEN =  "477abe9e7d27439681d62f4e0de1f5e1"
DEMO_API_HOST = 'https://demo.aeries.net/aeries.net/'

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.api = pyaeries.AeriesApi(host = DEMO_API_HOST, certifcate_auth_token = DEMO_CERTIFICATE_AUTH_TOKEN)


    def testGetSchools(self):
        schools = self.api.get_schools()

    def testGetSchoolTerm(self):
        schools = self.api.get_schools()

        if( len(schools) > 0):
            self.api.get_school_term(schools[0]['SchoolCode'])

    def testGetStudents(self):
        schools = self.api.get_schools()
        school_code = schools[3]['SchoolCode']

        students = self.api.get_students(school_code)
        self.assertTrue(len(students) > 0)

    def testGetStudentsByGradeLevel(self):
        schools = self.api.get_schools()
        school_code = schools[3]['SchoolCode']

        students = self.api.get_students_by_grade_level(school_code, 2)
        self.assertTrue(len(students) > 0)

    def testGetStudentsByStudentNumber(self):
        schools = self.api.get_schools()
        school_code = schools[3]['SchoolCode']

        students = self.api.get_students_by_student_number(school_code, 10)

        self.assertTrue(students[0]['LastName'] == u'Albright')

    def testGetStudentsExtended(self):
        schools = self.api.get_schools()
        school_code = schools[3]['SchoolCode']

        students = self.api.get_students_extended(school_code)
        self.assertTrue(len(students) > 0)


    def testGetStudentsExtendedByGradeLevel(self):
        schools = self.api.get_schools()
        school_code = schools[3]['SchoolCode']

        students = self.api.get_students_by_grade_level(school_code, 2)
        self.assertTrue(len(students) > 0)

    def testGetStudentsExtendedByStudentNumber(self):
        schools = self.api.get_schools()
        school_code = schools[3]['SchoolCode']

        students = self.api.get_students_by_student_number(school_code, 10)

        self.assertTrue(students[0]['LastName'] == u'Albright')




