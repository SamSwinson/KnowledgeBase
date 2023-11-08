names = list()

loop = 0

while loop == 0:
    name = input("Enter a name: ")
    if name == "done":
        loop = 1
        break
    names.append(name)

for i in range(len(names)):
    print (names[i])
