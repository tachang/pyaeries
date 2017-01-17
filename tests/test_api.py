import unittest
import logging
import pyaeries

from settings import API_HOST, CERTIFICATE_AUTH_TOKEN

log = logging.getLogger(__name__)

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.api = pyaeries.AeriesApi(host = API_HOST, certifcate_auth_token = CERTIFICATE_AUTH_TOKEN)


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
        students = self.api.get_students_by_grade_level(990, 2)
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


    def testGetTeachers(self):
        schools = self.api.get_schools()
        school_code = schools[3]['SchoolCode']
        teachers = self.api.get_teachers(school_code)
        self.assertTrue(len(teachers) > 0)

    def testGetStudentClassSchedules(self):
        """
        School Code | Number of Schedules
        0 0
        100 0
        200 0
        990 0
        991 0
        992 0
        993 0
        994 19804
        995 780
        996 6371
        997 10
        998 26
        999 0

        """

        class_schedules = self.api.get_student_class_schedules(997)

    def testGetCourses(self):
        courses = self.api.get_courses()

    def testGetCourseId(self):
        course = self.api.get_courses('e100')

    def testGetMasterScheduleSections(self):
        sections = self.api.get_master_schedule_sections(990)

