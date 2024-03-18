class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._courses = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def courses(self):
        return self._courses

    def add_course(self, course):
        self._courses.append(course)
