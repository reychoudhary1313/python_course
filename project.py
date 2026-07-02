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