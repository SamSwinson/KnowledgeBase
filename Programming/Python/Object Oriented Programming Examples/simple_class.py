class PartyAnimal():
    x = 0
    def party(self):
        self.x += 1
        print ("The value is:",self.x)

sam = PartyAnimal()
sam.party()
sam.party()
sam.party()
