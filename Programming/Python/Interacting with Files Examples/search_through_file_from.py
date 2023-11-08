file = open('mbox.txt', 'r')

for line in file:
    line = line.rstrip()
    if line.startswith('From: '):
        print (line)
