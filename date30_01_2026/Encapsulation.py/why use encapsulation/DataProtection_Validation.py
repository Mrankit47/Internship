# use encapsulation to protect and validate data

class student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0
    def set_gread(self,grade):
        if 0 <= grade <=100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")
    def get_grade(self):
        return self.__grade
    def get_status(self):
        if self.__grade>=60:
            return "passed"
        else:
            return "failed"
S = student("Ankit")
S.set_gread(27)
print(S.get_grade())
print(S.get_status())

        