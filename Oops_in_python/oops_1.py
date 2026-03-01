class employee:
    # constructor
    def __init__(self):
        self.id = 123
        self.salary = 1000
        self.designation= 'SDE'

    def salary_increment(self,incremented_salary):
        incremented_salary+= self.salary+(self.salary*10)/100
        return incremented_salary


# creating an instance of the class

# A function inside a class is called method

sam = employee()
salary_increment=0

salary_increment= sam.salary_increment(salary_increment)

print(f'Name  of the employee is {sam.id}, salary:{sam.salary} and having the designation of {sam.designation}')

print(f'incremented salary of the employee is {salary_increment}')


