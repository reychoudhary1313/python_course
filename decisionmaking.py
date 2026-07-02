"""age=20
if age>=18 :
    print("You are an adult.")

temperature=15 
if temperature>25:
    print("its hot outside.")
else:
    print("its cool outside.")

is_raining=True
if is_raining:
    print("take an umbrella.")
else:
    print("enjoy the sunshine.")

score=72
if score>=90:
    print("Grade A")
elif score>=75:
    print("Grade B")
elif score>=60:
    print("Grade C")    
else:
    print("Grade f")

#name= (input("what is your name :"))
#age= int(input("how old are you :"))
#if age<=18:
 #   print("Hello",name,"you are not an adult.")
#else:
 #   print("sorry",name,"you must be an adult.")"""

"""has_ticket = True
age=16

if age>=18 and has_ticket:
    print("Enjoy the show!")
elif has_ticket and age<18:
    print("You have a ticket but you're underage , you need a guardian.")
else:
    print("no ticket no entry")"""

"""is_member=True
balance=50
if is_member:
    if balance>=100:
        print("Purchase approved. Thank you , member!")
    else:
        print("You're a member but your balance is too low.")
else:
    print("please sign up for a membership first.")"""


"""num=int(input("Enter a number :"))
if num%2==0:
    print(num,"is an even number.")
else:    
    print(num,"is an odd number.")

temp=int(input("Enter the temperature :"))
if temp>30:
    print("drink water and stay hydrated.")
elif temp<10:
    print("wear warm clothes and stay cozy.")
else:
    print("Nice weather.")"""

"""password=int(123)
username=str("reyansh")
input_username=str(input("Enter your username :"))
input_password=int(input("Enter your password :"))
if input_username==username and input_password==password:
    print("Login successful. Welcome",input_username+"!")
    if input_username==username and input_password!=password:
        print("Incorrect password. Please try again.")
    elif input_username!=username and input_password==password:
        print("Username not found. Please try again.")
else:       
    print("Invalid username and password. Please try again.")"""

"""income=int(input("Enter your income :"))
if income<=25000:
    print("You are in the bracket 1 with no tax rate.")
elif income<=50000:
    print("You are in the bracket 2 with a tax rate of 10%.")
else:
    print("You are in the bracket 3 with a tax rate of 20%.")"""

#for i in range(1,5) :
#    print(i)

#for i in range (0,101,10):
 #   print(i)

name = input("Enter customer name: ")
age = int(input("Enter age: "))
show_time = input("Enter show time : ")

if age < 12:
    category = "Child"
    price = 100
elif age >= 60:
    category = "Senior"
    price = 120
else:
    category = "Adult"
    price = 200

if show_time == "morning":
    price = price * 0.8  

print(" TICKET SUMMARY")
print("Name     :", name)
print("Age      :", age)
print("Category :", category)
print("Show     :", show_time.capitalize())
print("Price    : ₹", price)

