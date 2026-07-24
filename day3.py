a=int(input("enter a number :"))
b=int(input("enter another number :"))
print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"x",b,"=",a*b)
name=input("enter your name :")
birth_year=int(input("enter your birthyear :"))
age=2026-birth_year
print("Your age is :",age)

celsius=int(input("enter a temperature in celsius :"))
farenheit=(celsius*9/5)+32
print("Temperature in fahrenheit :",farenheit)

item_name=input("enter the item name :")
price=int(input("enter the price of the item :"))
quantity=int(input("enter the quantity :"))
total=price*quantity
print(f"Total cost of {quantity} {item_name}(s) is : {total}")
subtotal = price * quantity
tax_amount = subtotal * 0.05        
grand_total = subtotal + tax_amount
print("grand total is :", grand_total)

#home work

name=input("enter your name :")
mark_1=int(input("enter the marks of math:"))
mark_2=int(input("enter the marks of science:"))
mark_3=int(input("enter the marks of english:"))
average=(mark_1+mark_2+mark_3)/3
print("you got :",average,"%")
if average>=80:
    print("excellent")
elif average>=60:
    print("good job")
else:
    print("keep practising")        
