#--------------------Spieler springen ------------

# eine Sprungvariable in Spieler Klasse anlegen
sprung = False

# und noch eine mit -16
sprungvar = -16

#in richtg braucht man auch einen Wert für springen

#-------------Spieler Klasse--------------

    def sprungSetzen(self):
        if self.sprungvar == -16:
            self.sprung = True
            self.sprungvar = 15
    def springen(self):
        if self.sprung:
            self.richtg = [0,0,0,1]
            if self.sprungvar >= -15:
                n = 1
                if self.sprungvar < 0:
                    n = -1
                self.y -= (self.sprungvar**2)*0.17*n
                self.sprungvar -= 1
            else:
                self.sprung = False