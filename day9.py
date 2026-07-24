"""unique_visitors={"reyansh","vikram","meena"}

print (unique_visitors)
unique_visitors.add("tara")
print(unique_visitors)
unique_visitors.remove("reyansh")
print(unique_visitors)"""

#colors = ["red", "green", "blue"]
#print(colors[1])

#person = {"name": "Tara", "city": "Mumbai"}
#print(person["city"])


#numbers = {1, 2, 2, 3, 3, 3}
#print(numbers)


def total_price(prices):
    total = 0
    for price in prices:
        total = total + price
    return total

cart = [200, 450, 99]
print(total_price(cart))


student_grades = {}

student_grades["Aisha"] = 88
student_grades["Raj"] = 92
student_grades["Meera"] = 76

for name in student_grades:
    print(name, "scored", student_grades[name])


inventory = {"apples": 10, "bananas": 5}

print(inventory.get("apples"))     # 10
print(inventory.get("oranges"))    # None — no error!
print(inventory.get("oranges", 0)) # 0 — a safe default


classroom = {
    "Group A": ["Aisha", "Raj"],
    "Group B": ["Meera", "Kabir"]
}

classroom = {
    "Group A": ["Aisha", "Raj"],
    "Group B": ["Meera", "Kabir"]
}

for group in classroom:
    print(group + ":")
    for student in classroom[group]:
        print("  -", student)


def build_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    return contact

new_contact = build_contact("Zara", "9123456789", "zara@email.com")
print(new_contact["phone"])

fruits = {"apple","banana","cherry"}
companies = {"google","microsoft","apple"}
intersect = fruits.intersection(companies)
print(intersect)
