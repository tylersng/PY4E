class PartyAnimal:
    def __init__(self,nam):
        self.x = 0
        self.name = (nam)
        print(self.name,"constructed")
    def party(self): 
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        #before we initialize FootballFan we are init the PartyAnimal
        self.points = 0
        #extend the points
    #touchdown methods
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = FootballFan("Jim")
j.party()
j.touchdown()