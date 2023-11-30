class Student:
    school_name = "ABC"
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = Student("harry",20)
print('student:',s1.name,s1.age)
print('school name ',Student.school_name)
s1.name = "jeesee"
s1.age = 19
print('student details:\n',s1.name,s1.age)
Student.school_name = 'xyz'
print('school name ',Student.school_name)

