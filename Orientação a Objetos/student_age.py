class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
# getter
    @property
    def age(self):
        return self.__age

# setter
    @age.setter
    def age(self, age):
        if age > 0:   
            self.__age = age
        else:
            print('Invalid age')
            
            
            
stud = Student("Vanessa", 19)
print('Name:', stud.name, stud.age) # obtém idade usando getter
stud.age = 16 # altera idade usando setter
print('Name:', stud.name, stud.age) # obtém idade usando getter