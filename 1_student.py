def InStuNo(StudentNo):
    print("Number of Student"+ str(StudentNo))

def InStuInfo(StuName,StuId,StuDate,StuMonth,StuYear):
    print("Student Name:" + StuName)
    print("Student Id:" + StuId)
    print("Student DoB: " + str(StuDate) + "/"+ str(StuMonth) + "/" + str(StuYear))

def InCourseNo(StuCourse):
    print("Number of courses: " + str(StuCourse))

def InCourseInfo(StuCourseId,StuCourseName):
    print("Course name: " + StuCourseName)
    print("Course id: " + StuCourseId)


khoi1 = InCourseNo(2)
khoi2 = InStuInfo("USTH ICT1","Not-Vietnamese",19,6,2014)

khoi3 = InCourseNo(123)
khoi4 = InCourseInfo("advanced","abc")

def InputMarks(StuCourseId, mark):
    16

"""
List:
Courses
Students
Marks

"""
marks =[14,16]
print(marks)