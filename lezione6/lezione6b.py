class Student:
    def __init__(self,name:str, studyProgram:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = None
        self.gender = None
    
    def __str__(self):
        return f"Student(name={self.name},studyProgram={self.studyProgram}, age={self.age}, gender={self.gender})"

    def set_age(self, new_age:int):
        self.age = new_age
    
    def set_gender(self, new_gender:str):
        self.gender = new_gender

emanuele = Student("Emanuele", "Python")
alessandro = Student("Alessandro", "Python")
michele = Student("Michele", "Java")
emanuele.set_age(19)
emanuele.set_gender("M")
alessandro.set_age(25)
alessandro.set_gender("M")
michele.set_age(22)
michele.set_gender("M")
print(emanuele)
print(alessandro)
print(michele)