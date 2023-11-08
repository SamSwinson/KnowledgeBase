numbers = [55,33,27,65,345,87,22,456,]
running_total = 0
count = 0

for number in numbers:
    running_total = running_total + number
    count += 1
    print(count, running_total)

total = running_total/count
print("The average number is: ", total)
