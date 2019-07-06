#Class
#Jacob Norenberg
#July 3, 2019

class student:
    def __init__(self):
            self.id = input("student id: ")
            self.gpa = input("student gpa: ")
            self.name = input("student name: ")
            self.units = input("student units: ")

    def showStudent(self):
        print("\nstudent id: ", self.id)
        print("student gpa: ", self.gpa)
        print("student name: ", self.name)
        print("student units: ", self.units)

student1=student()
student2=student()

student1.showStudent()
student2.showStudent()
