class Student:
    def __init__(self, name, marks, password):
        self.name = name          # public
        self._marks = marks       # protected
        self.__password = password  # private

    # public method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self._marks)

    # private method
    def __check_password(self):
        print("Password:", self.__password)

    # public method
    def login(self):
        self.__check_password()


class Result(Student):
    def grade(self):
        if self._marks >= 90:
            print("Grade: A")
        elif self._marks >= 80:
            print("Grade: B")
        elif self._marks >= 70:
            print("Grade: C")
        elif self._marks >= 60:
            print("Grade: D")
        else:
            print("Grade: F")


# Object creation
s = Result("Rahul", 90, "1234")

s.display()
s.grade()
s.login()