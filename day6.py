"""attempts = 0
correct_pin = "4321"
while True:
    entered_pin = input("enter your 4 digit pin:")
    attempts = attempts + 1

    if entered_pin == correct_pin:
        print("pin accepted")
        break

    if attempts == 3:
        print("too many attempts, card blocked")
        break

    print("incorrect pin , try again")"""

"""starting_number = int(input("enter the starting number:"))
while starting_number >= 0:
    print (starting_number)
    starting_number = starting_number - 1
print("lift off!")"""


"""secret_number = 42
attempts = 0
while True:
    guess = int(input("Guess the secret number between 1 and 100: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("congratulations! you guessed the secret number!")
        break
     
    elif guess < secret_number:
        print("too low")

    else:
        print("too high")

    if attempts == 7 :
        print("you ran out of attempts !")"""

total = 0
for i in range(1,4):
    total = total + i
    print(total)




    
    



 