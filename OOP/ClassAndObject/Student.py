class Student:
    def __init__(self, name, major, gpa):
        # self is a reference to the instance of the object
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

