class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll, course, marks, fees):
        super().__init__(name, age)
        self.roll = roll
        self.course = course
        self.marks = marks          # Public
        self.__fees = fees          # Private

    def display(self):
        print("\n----------------------------")
        print("Roll No :", self.roll)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Course  :", self.course)
        print("Marks   :", self.marks)

    def show_fees(self):
        print("Fees    :", self.__fees)

    def update_marks(self, marks):
        self.marks = marks


class Result(Student):
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"


class StudentManagement:

    def __init__(self):
        self.students = []

    # Add Student
    def add_student(self):
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        roll = int(input("Enter Roll No : "))
        course = input("Enter Course : ")
        marks = int(input("Enter Marks : "))
        fees = int(input("Enter Fees : "))

        s = Result(name, age, roll, course, marks, fees)
        self.students.append(s)

        print("Student Added Successfully!")

    # Display All
    def display_all(self):
        if len(self.students) == 0:
            print("No Student Found")
            return

        for s in self.students:
            s.display()
            s.show_fees()
            print("Grade   :", s.grade())

    # Search Student
    def search_student(self):
        roll = int(input("Enter Roll No : "))

        for s in self.students:
            if s.roll == roll:
                s.display()
                s.show_fees()
                print("Grade :", s.grade())
                return

        print("Student Not Found")

    # Update Marks
    def update_student(self):
        roll = int(input("Enter Roll No : "))

        for s in self.students:
            if s.roll == roll:
                marks = int(input("Enter New Marks : "))
                s.update_marks(marks)
                print("Marks Updated")
                return

        print("Student Not Found")

    # Delete Student
    def delete_student(self):
        roll = int(input("Enter Roll No : "))

        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)
                print("Student Deleted")
                return

        print("Student Not Found")

    # Menu
    def menu(self):

        while True:

            print("\n========== STUDENT MANAGEMENT ==========")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Update Marks")
            print("5. Delete Student")
            print("6. Exit")

            choice = int(input("Enter Choice : "))

            if choice == 1:
                self.add_student()

            elif choice == 2:
                self.display_all()

            elif choice == 3:
                self.search_student()

            elif choice == 4:
                self.update_student()

            elif choice == 5:
                self.delete_student()

            elif choice == 6:
                print("Thank You!")
                break

            else:
                print("Invalid Choice")


# Driver Code
obj = StudentManagement()
obj.menu()