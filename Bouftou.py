import random

class Bouftou :
    def __init__(self,PV = random.randint(170,280),PA = 5,PM = 4) :
        self.PV = PV
        self.PA = PA
        self.PM = PM

    def morsure (self):
        print("Je mords !")

class BouftouNoir (Bouftou):
    def __init__(self) :
        super().__init__(random.randint(150,250),5,3) 

    def mordillement (self):
        print("Je mordille !")
    
    def crachouille (self):
        print("Je crachouille !")

class BouftouRoyal (Bouftou):
    def __init__(self) :
        super().__init__(random.randint(610,900),7,5) 

    def guerison_bouftou (self) :
        print("Je me soigne")

    def abolissement (self):
        pass



b1 = Bouftou()
b2 = Bouftou()
b3 = Bouftou()

bn1 = BouftouNoir()
bn2 = BouftouNoir()

br = BouftouRoyal()

b1.morsure()
b2.morsure()
b3.morsure()

bn1.mordillement()
bn2.crachouille()

br.guerison_bouftou()

