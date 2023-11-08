import re
file = open("mbox-short.txt", "r")
matches = list()

for line in file:
    line = line.strip()
    word = re.findall ("^From: (\S+@|S+)", line)
    if len(word) != 1:  continue
    matches.append(word)

for match in matches:
    print (match)
