"""num = [1,2,3,4,5]
for i in num:
 if i%2 == 0:
    print(" it is an even number.")
 else:
    print(" it is an odd number.")

info = {
    "name":"Reyansh",
    "age":"14",
    "hobby":"Playing football"
}
print(f"My name is {info['name']}. I am {info['age']} years old and I like to {info['hobby']}.")


def total_score(scores):
   average = sum(scores)/len(scores)
   return average
scores = [85, 90, 78, 92, 85]

print(total_score(scores))


phone_book = {
   "reyansh":"1234567890",
   "tarun":"9876543210",
   "rohit":"4567891230"
}

user_asked_num = input("Enter the name of the person you want to call :")
if user_asked_num in phone_book:
    print(f"Calling {phone_book[user_asked_num]}.")
else:
    print("Number not found in the phone book.")"""


inventory_tracker ={
   "apple": 50,
   "banana": 30,
   "orange": 20,
   "grapes": 15
} 


print("1.Add an item")
print("2.Remove an item")
print("3.view all items")

while True:
    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        item_name = input("Enter the name of the item to add: ")
        item_quantity = int(input("Enter the quantity of the item: "))
        inventory_tracker[item_name] = item_quantity
        print(f"{item_name} added to inventory with quantity {item_quantity}.")

    elif choice == 2:
        item_name = input("Enter the name of the item to remove: ")
        if item_name in inventory_tracker:
            inventory_tracker.pop(item_name)
            print(f"{item_name} removed from inventory.")
        else:
            print(f"{item_name} not found in inventory.")

    elif choice == 3:
        print("Current inventory:")
    for item, quantity in inventory_tracker.items():
        print(f"{item}: {quantity}")

    else:
        print("Invalid choice.Enter a valid choice.")
    