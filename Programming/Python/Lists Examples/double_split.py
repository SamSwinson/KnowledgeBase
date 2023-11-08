text = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
textlist = list()
textlist = text.split()
email = textlist[1]
emaillist = email.split('@')
domain = emaillist[1]
print(domain)
