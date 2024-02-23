import random
cnumber=random.randrange( 1,101)
userinput=int(input("Enter your number: "))
if userinput>cnumber:
    print("computer number",cnumber)
    print("your guess number is too high")
elif cnumber>userinput:
    print("computer number",cnumber)
    print("your guess number is low")
else:
    print("computer number",cnumber)
    print("your guess number is equal")