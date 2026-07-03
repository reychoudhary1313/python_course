students = {
    "Reyansh":{
        "age":14,
        "grade":9
    },
    "Aryan":{
        "age":14,
        "grade":9
    }
}

def add_student(name,age,grade):
    students[name] = {
        "age":age,
        "grade":grade
    }
    return students
print(add_student("Tarun",15,10))

def print_all_students(students):
    for key,value in students.items():
        print(f"Name: {key}, Age: {value['age']}, Grade: {value['grade']}")
print_all_students(students)

def find_student(students,name):
    result = students.get(name)
    if result is None:
       return "not found"
    return result
print(find_student(students,"Reyansh"))



students = {}
grades = set()

def students_in_grade(students, grade):
    names = []

    for name in students:
        if students[name]["Grade"] == grade:
            names.append(name)

    return names

while True:
    print("1. Add Student")
    print("2. Search Student")
    print("3. List Students")
    print("4. Show Students in a Grade")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")

        students[name] = {
            "Age": age,
            "Grade": grade
        }

        grades.add(grade)

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            print(students[name])
        else:
            print("Student not found.")

    elif choice == "3":
        for name in students:
            print(name, students[name])

    elif choice == "4":
        grade = input("Enter grade: ")
        print(students_in_grade(students, grade))

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

