class Student: 
    count = 0

def _init_(self, name, age, Language, city):
self.name = name
self.age = age
self.language = language
self.city =city
Student.count += 1


def _str_(self):
return f"Name:{self.name},  Age: {self.age}, Language: {self.language}, City: {self.city}"

@staticmethod
def get_total_students_Class(cls):
    return cls.count

@Classmethod
def get_total_students():
    return Student.count

if _name. == '_main_':
estudiante = Student( name:'Juan', age: 21, language:'Python', city:'Math')
print(Student.get_total_students())
print(Student.get_total_students_class())

estudiante.name = "Josesito"


estudiante2 = Student( name:'Ana', age: 21, language:'Python', city:'Math')
print(Student.get_total_students())
print(Student.get_total_students_class())
