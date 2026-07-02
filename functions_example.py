"""def square(number):
    return number * number

result = square(6)
print(result)"""

"""def calculate_total(price, quantity):
    total = price * quantity
    return total

bill = calculate_total(150, 3)
print("Your total is: ₹" + str(bill))"""

"""def make_coffee(size="Medium"):
    print("Making a " + size + " coffee.")

make_coffee()
make_coffee("Large")"""

"""def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))   # 9 + 16 = 25"""

"""def get_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(get_factorial(5))   # 5 x 4 x 3 x 2 x 1 = 120"""


def calculate_discount(price , discount_percent):
    final_price=price - (price * discount_percent / 100)
    return final_price
print(calculate_discount(100,30))

def count_vowels(word):
    vowels=str("a,e,i,o,u")
    count=0
    for i in word:
        if i in vowels:
            count=count+1
    return count 
print (count_vowels("abce"))  

def max_of_three(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    elif c>a and c>b:
        print(c)
    
max_of_three(23,17,16)



