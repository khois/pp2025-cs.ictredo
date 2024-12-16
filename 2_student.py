class Student:
    def __init__(self,StuName,StuId,StuDate,StuMonth,StuYear):
        self._StudName = StuName
        self._StudId = StuId
        self._StudDate = StuDate
        self._StudMonth = StuMonth
        self._StudYear = StuYear

    def __str__(self) -> str:
        return f"My name is {self._StudName},id {self._StudId}. My birthday is {self._StudDate}/{self._StudMonth}/{self._StudYear}"

class Course:
    def __init__(self,StuCourseId,StuCourseName ):
        self._CourseName = StuCourseName
        self._CourseId = StuCourseId

    def __str__(self) -> str:
        pass
    
khoi = Student("USTH ICT1", "Not-Vietnamese", 19, 6,2014)
adv = Course("advanced", 123)

print(khoi)

"""
List:
Courses
Students
Marks

"""

Courses = [adv]
Students = [khoi,"a"]




