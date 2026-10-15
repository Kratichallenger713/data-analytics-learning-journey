class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display(self):
        print("Name  :", self.name)
        print("Age   :", self.age)
        print("Email :", self.email)


class Employee(Person):

    def __init__(self, emp_id, name, age, email, department, salary):
        super().__init__(name, age, email)

        self.emp_id = emp_id
        self.department = department
        self.__salary = salary   # private variable

    # Encapsulation
    def get_salary(self):
        return self.__salary

    def update_salary(self, salary):
        self.__salary = salary

    def display_employee(self):
        print("\n----------------------------")
        print("Employee ID :", self.emp_id)
        super().display()
        print("Department  :", self.department)
        print("Salary      :", self.__salary)


class Manager(Employee):

    # Polymorphism (method overriding)
    def calculate_bonus(self):
        return self.get_salary() * 0.20


class EmployeeManagement:

    def __init__(self):
        self.employees = []


    # Add Employee
    def add_employee(self):

        emp_id = int(input("Enter Employee ID : "))
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        email = input("Enter Email : ")
        department = input("Enter Department : ")
        salary = int(input("Enter Salary : "))

        emp = Manager(
            emp_id,
            name,
            age,
            email,
            department,
            salary
        )

        self.employees.append(emp)

        print("Employee Added Successfully!")


    # Display Employees
    def display_all(self):

        if len(self.employees) == 0:
            print("No Employee Found")
            return

        for emp in self.employees:
            emp.display_employee()
            print("Bonus       :", emp.calculate_bonus())


    # Search Employee
    def search_employee(self):

        emp_id = int(input("Enter Employee ID : "))

        for emp in self.employees:

            if emp.emp_id == emp_id:
                emp.display_employee()
                return

        print("Employee Not Found")


    # Update Salary
    def update_salary(self):

        emp_id = int(input("Enter Employee ID : "))

        for emp in self.employees:

            if emp.emp_id == emp_id:

                salary = int(input("Enter New Salary : "))

                emp.update_salary(salary)

                print("Salary Updated")
                return

        print("Employee Not Found")


    # Delete Employee
    def delete_employee(self):

        emp_id = int(input("Enter Employee ID : "))

        for emp in self.employees:

            if emp.emp_id == emp_id:

                self.employees.remove(emp)

                print("Employee Deleted")
                return

        print("Employee Not Found")


    # Menu
    def menu(self):

        while True:

            print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")

            print("1. Add Employee")
            print("2. Display All Employees")
            print("3. Search Employee")
            print("4. Update Salary")
            print("5. Delete Employee")
            print("6. Exit")


            choice = int(input("Enter Choice : "))


            if choice == 1:
                self.add_employee()

            elif choice == 2:
                self.display_all()

            elif choice == 3:
                self.search_employee()

            elif choice == 4:
                self.update_salary()

            elif choice == 5:
                self.delete_employee()

            elif choice == 6:
                print("Thank You!")
                break

            else:
                print("Invalid Choice")


# Main Program

system = EmployeeManagement()

system.menu()