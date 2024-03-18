import Student as St
import Course as Cr

def add_student():
    name = input("Entrez le nom de l'étudiant: ")
    age = input("Entrez l'âge de l'étudiant: ")
    try:
       if not isinstance (age,int) :
        return
       elif age < 0:
            print("Veuillez entrer un âge positif.")
            return
    except :
        pass
        
    
    student = St.Student(name, age)
    St.students.append(student)

def add_course():
    name = input("Entrez le nom du cours: ")
    credits = input("Entrez le nombre de crédits du cours: ")
    try:
        credits = int(credits)
        if credits < 0:
            print("Veuillez entrer un nombre de crédits positif.")
            return
    except ValueError:
        print("Le nombre de crédits doit être un entier.")
        return
    
    course = Cr.Course(name, credits)
    Cr.courses.append(course)

def assign_course():
    if not St.students:
        print("Aucun étudiant n'est disponible.")
        return
    
    print("Sélectionnez un étudiant:")
    for i, student in enumerate(St.students):
        print(f"{i+1}. {student.name}")
    student_choice = input("Votre choix : ")
    try:
        student_choice = int(student_choice) - 1
        if student_choice < 0 or student_choice >= len(St.students):
            raise ValueError
    except ValueError:
        print("Choix invalide.")
        return

    if not Cr.courses:
        print("Aucun cours n'est disponible.")
        return
    
    print("Sélectionnez un cours:")
    for i, course in enumerate(Cr.courses):
        print(f"{i+1}. {course.name}")
    course_choice = input("Votre choix : ")
    try:
        course_choice = int(course_choice) - 1
        if course_choice < 0 or course_choice >= len(Cr.courses):
            raise ValueError
    except ValueError:
        print("Choix invalide.")
        return

    St.students[student_choice].add_course(Cr.courses[course_choice])

while True:
    print("\nMenu de choix :")
    print("1. Ajouter un étudiant")
    print("2. Ajouter un cours")
    print("3. Assigner un cours à un étudiant")
    print("4. Quitter")
    choice = input("Entrez votre choix : ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        assign_course()
    elif choice == "4":
        break
    else:
        print("Choix invalide.")

print("\nÉtudiants et leurs cours:")
for student in St.students:
    print(f"Étudiant: {student.name}, Age: {student.age}, Cours: {[course.name for course in student.courses]}")
