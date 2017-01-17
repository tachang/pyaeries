import requests


class AeriesApi(object):
    
    API_HOST = 'https://demo.aeries.net/aeries.net/'
    API_PREFIX = 'api/v2/'

    def __init__(self, host, certifcate_auth_token):

        self.host = host
        self.certifcate_auth_token = certifcate_auth_token
        self.api_url = self.API_HOST + self.API_PREFIX

    @property
    def headers(self):
        return {
            'AERIES-CERT': self.certifcate_auth_token
        }

    def get_students(self):
        return []

    def get_schools(self, school_code=''):
        r = requests.get(self.api_url + 'schools/{}'.format(school_code), headers=self.headers)
        return self.process_response(r)

    def get_school_term(self, school_code):
        r = requests.get(self.api_url + 'schools/{}/terms'.format(school_code), headers=self.headers)
        return self.process_response(r)

    def get_students(self, school_code, student_id=''):
        r = requests.get(self.API_HOST + 'api/schools/{}/students/{}'.format(school_code, student_id), headers=self.headers)
        return self.process_response(r)

    def get_students_by_grade_level(self, school_code, grade_level):
        r = requests.get(self.API_HOST + 'api/schools/{}/students/grade/{}'.format(school_code, grade_level), headers=self.headers)
        return self.process_response(r)

    def get_students_by_student_number(self, school_code, student_number):
        r = requests.get(self.API_HOST + 'api/schools/{}/students/sn/{}'.format(school_code, student_number), headers=self.headers)
        return self.process_response(r)


    def get_students_extended(self, school_code, student_id=0):
        url = self.api_url + 'schools/{}/students/{}/extended'.format(school_code, student_id)
        r = requests.get(url, headers=self.headers)
        return self.process_response(r)

    def get_students_extended_by_grade_level(self, school_code, grade_level):
        r = requests.get(self.api_url + 'schools/{}/students/grade/{}/extended'.format(school_code, grade_level), headers=self.headers)
        return self.process_response(r)

    def get_students_extended_by_student_number(self, school_code, student_number):
        r = requests.get(self.api_url + 'schools/{}/students/sn/{}/extended'.format(school_code, student_number), headers=self.headers)
        return self.process_response(r)


    def get_student_data_changes(self):
        raise Exception('Not implemented')

    def get_student_enrollment_history(self):
        raise Exception('Not implemented')

    def get_student_contacts(self):
        raise Exception('Not implemented')

    def get_student_programs(self):
        raise Exception('Not implemented')

    def get_student_test_scores(self):
        raise Exception('Not implemented')

    def get_student_class_schedules(self, school_code, student_id=''):
        r = requests.get(self.API_HOST + 'api/schools/{}/classes/{}'.format(school_code, student_id), headers=self.headers)
        return self.process_response(r)

    def get_courses(self, course_id=''):
        r = requests.get(self.API_HOST + 'api/courses/{}'.format(course_id), headers=self.headers)
        return self.process_response(r)

    def get_course_data_changes(self, year, month, day, hour, minute):
        kwargs = {
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'minute': minute
        }
        r = requests.get(self.api_url + 'coursedatachanges/{year}/{month}/{day}/{hour}/{minute}'.format(**kwargs), headers=self.headers)
        return self.process_response(r)

    def get_staff(self):
        raise Exception('Not implemented')

    def get_staff_data_changes(self):
        raise Exception('Not implemented')

    def get_teachers(self, school_code, teacher_number=''):
        r = requests.get(self.API_HOST + 'api/schools/{}/teachers/{}'.format(school_code, teacher_number), headers=self.headers)
        return self.process_response(r)

    def get_teachers_with_staffid(self):        
        raise Exception('Not implemented')

    def get_master_schedule_sections(self, school_code, section_number=''):
        r = requests.get(self.API_HOST + 'api/schools/{}/sections/{}'.format(school_code, section_number), headers=self.headers)
        return self.process_response(r)

    def get_master_schedule_sections_changes(self):
        raise Exception('Not implemented')

    # def get_student_class_schedules(self):
    #     """
    #     Section Class Roster
    #     Class Schedules/History
    #     """
    #     raise Exception('Not implemented')

    def get_student_class_schedules_changes(self):
        raise Exception('Not implemented')

    def get_codes(self):
        raise Exception('Not implemented')

    def get_gradebooks(self):
        raise Exception('Not implemented')

    def get_gradebook_assignments(self):   
        raise Exception('Not implemented')


    def get_gradebook_finalmarks(self):   
        raise Exception('Not implemented')


    def get_students_for_gradebook(self):
        """
        A method of retrieving students for ALL gradebooks for a school or district is not possible. It is
        recommended that this API be called on the fly when needed by your system. 
        """
        raise Exception('Not implemented')


    def get_assignment_scores(self):
        """
        A method of retrieving Scores for ALL assignments in a gradebook is not possible. It is recommended
        that this API be called on the fly when needed by your system. 
        """
        raise Exception('Not implemented')


    def create_assignment_score_update(self):
        raise Exception('Not implemented')

    def process_response(self, r):
        r.raise_for_status()
        return r.json()
        