def hello(language):
    if language == 'sp':
        return "Hola"
    elif language == 'fr':
        return "Bonjour"
    else:
        return "Hello"

print(hello('sp'), "Sam")
print(hello('fr'), "Sam")
print(hello('en'), "Sam")
