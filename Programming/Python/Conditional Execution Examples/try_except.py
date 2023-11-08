number = input("Please enter a number: ")

try:
    #you can't add a number to a string so if the number variable is a string then it converts it to an integer
    number = number + 1
except:
    numberint = int(number)

if numberint == 10:
    print("Your number is equal to 10")
elif numberint > 10:
    print("Your number is greater than 10")
else:
    print ("Your number is less than 10")
