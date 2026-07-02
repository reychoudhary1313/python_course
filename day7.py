"""def cube(number):
    return number*number*number

print(cube(2))

def print_seperator():
    print("-"*20)

print("my name is Reyansh")
print_seperator()
print("I love to play football.")

def convert_celsius_to_farenheit(celsius):
    f= celsius * 9/5 + 32

    return f

print(convert_celsius_to_farenheit(23))

def is_prime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number % i ==0:
            return False
    return True

print(is_prime(23))"""

def km_to_miles(km):
    return km*0.621371

def kg_to_pounds(kg):
    return kg*2.20462

def celsius_to_farenheit(c):
    return c*9/5+32


print("===unit converter===")
print("1.Kilometers to miles")
print("2.kilograms to pounds")
print("3.Celsius to farenheit")

choice = input("choose an option(1-3):")

if choice == "1":
    value = float(input("enter value in km:"))
    result = km_to_miles(value)
    print(str(value) + "km is equal to" + str(result) + "miles")

elif choice == "2":
    value = float(input("enter the value of kgs:"))
    result = kg_to_pounds(value)
    print(str(value) + " kg is equal to" + str(result) + "pounds")

elif choice == "3":
    value = float(input("enter the value of celsius:"))
    result = celsius_to_farenheit(value)
    print(str(value) + "celsius is equal to" + str(result) + "pounds")

else :
    print("invalid choice")
    

