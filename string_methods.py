name = "Arjen Robben"
print(name.upper())

favourite_movies = ["housefull 4","maidaan","dhurandhar","84","phir hera pheri"]
print(favourite_movies[0])
print(favourite_movies[-1])

books = {
    "book":"the autobiogaphy of Robben - the cut in god",
    "author":"fabrizio romano",
    "year":"2020"
}
print(f"my favourite book is{books['book']}.")


def add_student(roster,name):
    roster.append(name)
    return roster

students = []
students = add_student(students,"reyansh")
print(students)



items = {
    "football":20,
    "tennis ball":35,
    "leather ball":10
}

for key in items:
   price = items[key]*0.9
   print(key,"now costs Rs" + str(price))

student_who_submitted_homework = {"Tarun","Reyansh","Rohit","Aman"}
all_students = {"Siddharth","Avanish","Rohan","Krish","Tarun","Reyansh","Rohit","Aman"}

print(all_students - student_who_submitted_homework)
