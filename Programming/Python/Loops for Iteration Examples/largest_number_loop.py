numbers = [55,33,27,65,345,87,22,456,]
largest_number = None

for number in numbers:
    if largest_number is None:
        largest_number = number
    elif number > largest_number:
        largest_number = number
    print(largest_number, number)

print(largest_number)
