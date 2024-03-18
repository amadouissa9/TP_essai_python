class Course:
    def __init__(self, name, credits):
        self._name = name
        self._credits = credits

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, value):
        self._credits = value

def add_student():
    name = input("Entres le nom de l'etudiant: ")
    age = int(input("Entrez l'age de l'etudiant: "))
    student = add_student.Student(name, age)
    students.append(student)

def add_course():
    name = input("Entrez le nom du cour : ")
    credits = int(input("Entrez le credit credits: "))
    course = Course(name, credits)
    courses.append(course)

def assign_course():
    print("Selection l'etudiant:")
    for i, student in enumerate(students):
        print(f"{i+1}. {student.name}")
    student_choice = int(input()) - 1
    print("Selrctionner un cour:")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course.name}")
    course_choice = int(input()) - 1
    students[student_choice].add_course(courses[course_choice])

students = []
courses = []
