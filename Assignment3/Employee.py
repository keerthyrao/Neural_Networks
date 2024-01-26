class Employee:
    no_of_employees = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.no_of_employees += 1

    @staticmethod
    def average_salary(femployees, n):
        add = 0
        for employee in femployees:
            add += employee.salary
        return add / n


class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department)

def main():
    femployees = []
    employees = []
    femp1 = FulltimeEmployee("Sara", "Johnson", 75000, "Team Lead")
    femployees.append(femp1)
    femp2 = FulltimeEmployee("Emily", "Brown", 120000, "Manager")
    femployees.append(femp2)
    femp3 = FulltimeEmployee("Ashley", "Taylor", 90000, "Project Lead")
    femployees.append(femp3)
    femp4 = FulltimeEmployee("Megan", "Thompson", 150000, "hr")
    femployees.append(femp4)
    employee1 = Employee("David", "Wilson", 70000, "Developer")
    employees.append(employee1)
    employee2 = Employee("Brian", "Miller", 60000, "Tester")
    employees.append(employee2)
    print("Average salary of fulltime employees:", FulltimeEmployee.average_salary(femployees, (len(femployees))))
    print("Average salary of employees:", Employee.average_salary(employees, (len(employees))))

if __name__ == "__main__":
    main()
