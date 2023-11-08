numbers = [55,33,27,65,345,87,22,456,]
smallest_number = None

for number in numbers:
    if smallest_number is None:
        smallest_number = number
    elif number < smallest_number:
        smallest_number = number
    print(smallest_number, number)

print(smallest_number)
