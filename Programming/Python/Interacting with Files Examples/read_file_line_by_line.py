file = open('mbox.txt', 'r')

for line in file:
    line = line.rstrip()
    print (line)
