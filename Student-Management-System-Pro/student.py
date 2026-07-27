class student:
    def __init__(self,roll_no,name,age,email,course,marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.email = email
        self.course = course
        self.marks = marks

    def display(self):
        print("\n---- Student Details------")
        print("Roll No :",self.roll_no)
        print("Name :", self.name)
        print("Age :",self.age)
        print("Email :",self.email)
        print("Course : ",self.course)
        print("Marks :",self.marks)
        