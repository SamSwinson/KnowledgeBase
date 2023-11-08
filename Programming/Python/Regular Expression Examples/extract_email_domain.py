import re
file = open("mbox-short.txt", "r")
matches = list()

for line in file:
    line = line.strip()
    word = re.findall ("@([^ ]*)", line)
    print(word)
    if len(word) != 1:  continue
    matches.append(word)

for match in matches:
    print (match)
