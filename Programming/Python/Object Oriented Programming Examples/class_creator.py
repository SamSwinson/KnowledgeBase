class PartyAnimal():
    x = 0
    def __init__(self):
        print("Class has been created")
        
    def party(self):
        self.x += 1
        print ("The value is:",self.x)

sam = PartyAnimal()
sam.party()
