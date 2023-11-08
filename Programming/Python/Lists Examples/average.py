numbers = list()
loop = 0
while loop == 0:
    number = input("Enter a number: ")
    if number == 'done':    break
    numberint = int(number)
    numbers.append(numberint)

print(sum(numbers)/len(numbers))
