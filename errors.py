#typeError
"""age = 14
print("i am" + age + "years old") 
print("I am " + str(age) + " years old")"""

#KeyError
"""student = {
    "name":"reyansh",
    "age": 14
}
 
print(student.get('grade'))"""

#NameError
"""def greet(name):
    print("Hello" + Name)# here it will call a Error because we have used "Name insted of "name

greet("Reyansh")

    """

"""def calculate_average(scores):
    print("debug scores",scores,type(scores))
    total = 0
    for score in scores:
        total = total + score
    average = total / len (scores)
    return average
result = calculate_average(["70",80,90])

print("average",result)"""



"""def get_average(scores):
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)

def is_passing(average):
    return average >= 50

def print_result(name,average):
    status = "PASS" if is_passing(average) else "FAIL"
    print(name + "- Average:" + str(average) + "-" + status)

name = input("Enter student name:")
scores = []
for i in range(3):
    score = int(input("enter score" + str(i + 1) + ": "))
    scores.append(score)

average = get_average(scores)
print_result(name,average)


#   Messy - hard to read , cryptic names, no structure
def f(d):
    r = []
    for k in d:
        if d[k]["g"] == "9th":
            r.append(k)
    return r

#Clean - same logic , easy to read

def find_student_in_grade(students,target_grade):
    matching_students = []
    for name in students:
        if students[name]["grade"]   == target_grade:
            matching_students.append(name)
    return matching_students

def calculate_discount(price,discount_percent):
    discount = price * (discount_percent/100)
    final = price - discount
    return final

products = {
    "pen": 10,
    "notebook": 50,
    "bag": 500
}

for product in products:
    discounted = calculate_discount(products[product],10)
    print(product + "discount price:" + str(discounted))"""


#problem:Given a dictionary of student names and thier scores, print only students who passed (acore>=50),with thier grade letter

def get_grade_letter(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def print_passing_students(students):
    print("\n---- Passing students ----")
    found_any = False 
    for name in students:
        score = students[name]
        if score >= 50:
            grade = get_grade_letter(score)
            print(name + ":" + str(score) + "(" + grade + ")")
            found_any = True
    if not found_any:
            print("no students passed.")  
results = {
    "Aisha": 88,
    "Raj": 45,
    "Meera": 72,
    "Kabir":91,
    "Zara": 38
}


print_passing_students(results)
