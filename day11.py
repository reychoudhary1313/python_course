# TypeError where it shows that a string() and int() cannot be concatenated together
"""age = 14
print("reyansh is " + age)"""

#fixing it by using typecasting
"""age = 14
print("reyansh is " + str(age))


num1= int(input("Enter first number :"))
num2= int(input("Enter second number :"))

if num2 == 0:
    print("Division by zero is Prohibited.")
else:
    result = num1 / num2
    print("Result:", result)"""




"""def safe_get_score(students,name):
    result = students.get(name)
    if result is None:
        return "not found"
    return result 

scores = {
        "Reyansh": 94,
        "Anjali": 88,
        "Rohan": 76
    }
print(safe_get_score(scores,"Reyansh"))
print(safe_get_score(scores,"tarun"))"""




def add_student(name,score):
    name = input("Enter student name:")
    score = input("Enetr the student's score")

    class_1[name]=score
    return class_1 

def lookup_student(class_1,name):
    result = class_1.get(name)
    if result is None:
        return "Student not found"
    return result

def get_highest(class_1):
    top_name = ""
    top_score = -1
    for name in class_1:
        if class_1[name] > top_score:
            top_score = class_1[name]
    return top_name,top_score


def get_lowest(class_1):
    low_name = ""
    low_score = 101
    for name in class_1:
        if class_1[name] < low_score:
            low_score = class_1[name]
    return low_name,low_score

def get_average (class_1):
    total = 0
    for name in class_1:
        total = total + class_1[name]
    return total/len(class_1)


def print_summary(class_1):
    if len(class_1)==0:
        print("No students in class")
    return

    top_name,top_score = get_highest(class_1)
    low_name,low_score = get_lowest(class_1)

    print("--------class summary--------")
    print("highest :" + top_name +"(" + str(top_score) + ")")
    print("lowest :" + low_name + "(" + str(low_score) + ")")
    print("Average :" + str(round(average,2)))
    print("-----------------------------")


class_1 = {"Reyansh":94,"Tarun":95,"Eric":73 }

while True :
    print("what do you want to do")
    print("1.Add a student")
    print("2.Look up the score of a student")
    print("3.summarize the scores with highest,lowest and class average")
    print("4.Exit")

    choice = input("Enter your choices from 1-4(only give the option number):")

    if choice == "1":
        name = input("Enter the student's name :")
        score = int(input("Enter student's name :"))
        class_1 = add_student(class_1,name,score)
        print(name + "added with score" + str(score))

    elif choice == "2":
        name = input("Enter student name :")
        result = lookup_student(class_1,name)
        if result == "Student not found":
            print("Student not found")
        else:
            print(name + "scored" + str(result))
        
    elif choice == "3":
        print_summary(class_1)

    elif choice == "4":
        print("goodbye")
        break

    else:
        print("Invalid choice . Please enter from 1-4.")









        