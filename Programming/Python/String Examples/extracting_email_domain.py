email = 'sam.swinson@gmail.com '

atpos = email.find('@')
spacepos = email.find(' ')
domain = email[atpos : spacepos]
print(atpos)
print(spacepos)
print(email)
print(domain)
