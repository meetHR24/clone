Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

class Course:
...     def __init__(self, course_code, course_name, max_seats):
...         self.course_code = course_code
...         self.course_name = course_name
...         self.max_seats = max_seats
...         self.enrolled_students = []
... 
... class College:
...     def __init__(self):
...         self.students = {}
...         self.courses = {}
... 
...     def add_student(self, student_id, name):
...         student = Student(student_id, name)
...         self.students[student_id] = student
... 
...     def add_course(self, course_code, course_name, max_seats):
...         course = Course(course_code, course_name, max_seats)
...         self.courses[course_code] = course
... 
...     def enroll_student(self, student_id, course_code):
...         student = self.students.get(student_id)
...         course = self.courses.get(course_code)
...         if student and course:
...             if len(course.enrolled_students) < course.max_seats:
...                 course.enrolled_students.append(student)
...                 student.courses.append(course)
...                 return True
...             else:
...                 return "Course is full"
...         else:
...             return "Student or course not found"
... 
... 
... college = College()
... college.add_student("S001", "Alice")
... college.add_student("S002", "Bob")
... college.add_course("C101", "Introduction to Python", 3)
... college.add_course("C102", "Web Development Basics", 2)
... 
... enrollment_result = college.enroll_student("S001", "C101")
... print(enrollment_result)
... 
... 
... print(college.students)
... print(college.courses)
>>> [DEBUG ON]
>>> [DEBUG OFF]
