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




def safe_get_score(students,name):
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
print(safe_get_score(scores,"tarun"))




    