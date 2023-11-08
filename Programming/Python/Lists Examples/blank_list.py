names = list()

loop = 0

while loop == 0:
    name = input("Enter a name: ")
    if name == "done":
        loop = 1
        break
    names.append(name)

print (names)
print (names[2])
print (names[:2])
print (names[2:])
print (names[:])
print (len(names))
