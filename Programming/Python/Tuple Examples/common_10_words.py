filename = input("Enter filename with file extention: ")
try:
    file = open(filename, "r")
except:
    print("Please enter a valid filename and extention.")
    quit()

count = dict()
words = list()
commonwords = list()

for line in file:
    line = line.strip()
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

for k,v in count.items():
    tuple = (v, k)
    commonwords.append(tuple)

commonwords = sorted(commonwords, reverse = True)

for v, k in commonwords[:10]:
    print(k, v)
