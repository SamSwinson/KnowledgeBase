import re
file = open("mbox-short.txt", "r")

for line in file:
    line = line.strip()
    if re.search("^From:", line):
        print(line)
