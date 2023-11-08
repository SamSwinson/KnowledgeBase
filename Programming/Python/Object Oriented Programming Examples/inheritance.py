class PartyAnimal():
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print("Class has been created")

    def party(self):
        self.x += 1
        print (self.name, "value is:",self.x)

    def __del__(self):
        print("Class has been destroyed")

class NewParty(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points += 10
        self.party()
        print("Points:", self.points)


s = PartyAnimal("Sam")
s.party()

b = PartyAnimal("Bob")
s.party()
b.party()

a = NewParty("Alan")
a.touchdown()
s.party()
b.party()
a.touchdown()
