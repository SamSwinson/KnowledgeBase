text = input("Enter text: ")
words = text.split()
count = dict()

for word in words:
    count[word] = count.get(word, 0) + 1

bigword = None
bigcount = None
for aaa,bbb in count.items():
    print(aaa, bbb)
