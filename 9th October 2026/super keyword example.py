class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Developer(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language=language
d1=Developer("David","1000",'Python')
print(d1.language)
print(d1.name)
print(d1.salary)