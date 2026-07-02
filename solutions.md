for i in range (1,21):
    print(i)

count=0
while count < 5 :
    print("i love python") 
    count = count + 1

num2=int(input("Enter a number from 1 to 10 :"))
while num2 != 7:
    num2=int(input("Enter a number from 1 to 10 :"))
print("correct guess!")

for i in range(1,51):
    if i%5!=0:
        continue
    print(i)

for i in range(1,101):
    if i>30:
        break
    print(i)