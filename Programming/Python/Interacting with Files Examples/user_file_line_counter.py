
userfile = input('Enter your filename: ')
try:
    file = open(userfile, 'r')
except:
    print("Couldn't open filename:", userfile)
    quit()

count = 0
for line in file:
    count += 1
print("The number of lines in", userfile, "is:", count)
