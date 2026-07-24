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


def students_in_grade(students, grade):
    matches = []
    for name in students:
        if students[name]["grade"] == grade:
            matches.append(name)
    return matches


def get_all_grades(students):
    grades = set()
    for name in students:
        grades.add(students[name]["grade"])
    return grades


# --- Main menu ---

while True:
    print("\n--- Student Database Menu ---")
    print("1. View all students")
    print("2. Add a student")
    print("3. Search for a student")
    print("4. Find students by grade")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print_all_students(students)

    elif choice == "2":
        name  = input("Enter student name: ")
        age   = int(input("Enter age: "))
        grade = input("Enter grade (e.g. 9th): ")
        students = add_student(students, name, age, grade)
        print(name + " added successfully.")

    elif choice == "3":
        name   = input("Enter student name to search: ")
        result = find_student(students, name)
        if result == "Not found":
            print("Student not found.")
        else:
            print(name + ": Age " + str(result["age"]) + ", Grade " + result["grade"])

    elif choice == "4":
        grade   = input("Enter grade to search (e.g. 9th): ")
        matches = students_in_grade(students, grade)
        if len(matches) == 0:
            print("No students found in grade " + grade)
        else:
            print("Students in grade " + grade + ": " + ", ".join(matches))

    elif choice == "5":
        all_grades = get_all_grades(students)
        print("\nGrades represented in this database: " + str(all_grades))
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")