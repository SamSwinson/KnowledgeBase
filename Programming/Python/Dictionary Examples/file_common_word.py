filename = input("Enter filename with file extention: ")
try:
    file = open(filename, "r")
except:
    print("Please enter a valid filename and extention.")
    quit()

count = dict()
words = list()

for line in file:
    line = line.strip()
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

bigword = None
bigcount = None
for aaa,bbb in count.items():
    if bigcount == None or bigcount < bbb:
        bigcount = bbb
        bigword = aaa

print (bigword, bigcount)
