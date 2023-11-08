file = open('mbox.txt', 'r')

for line in file:
    line = line.rstrip()
    if not line.startswith('Subject: '):
        continue
    print (line)
