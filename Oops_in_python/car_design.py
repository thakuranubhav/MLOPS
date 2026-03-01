class Student:
    __name = "Anubhav"

    def __init__(self, name):
        self.name = name
        self.age = 23

    def __hello(self):
        print("How are you")

    def welcome(self):
        self.__hello()

s1 = Student("virat kohli")

print(Student._Student__name)  
print(s1._Student__name)        