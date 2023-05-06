"""
WAP to find factors of given number.
Write a Python function student_data () which will print the id of a student (student_id).
If the user passes an argument student_name or student_class the function will print the student name and class.
"""


class Factors:

    def find_factor(self, input_num):
        return list(filter(lambda x: input_num % x == 0, range(2, int(input_num / 2) + 1)))

class Student:

    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
        self.info = {"student_id": self.student_id, "student_name": self.student_name,
                     "student_class": self.student_class}
    def __str__(self):
        return f"<Name : {self.student_name}, Class: {self.student_class}, Id : {self.student_id}>"
    def student_data(self, *args):
        return [arg + " : " + self.info[arg] for arg in args]

if __name__ == "__main__":
    f = Factors()
    print(f.find_factor(1234))
    x = Student(1234, "Yash", "SE_IT_B")
    y = x.student_data("student_name", "student_class")
    print(y)


