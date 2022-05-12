class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.__salary = salary
        self.project = project

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def work(self):
        print("Name", self.name, "Salary", self.__salary, "Project", self.project)


emp = Employee("Aditya", 1000, "NLP")

emp.set_salary(2000)
emp.get_salary()
emp.work()