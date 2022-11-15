#--------------- Spieler bewegung---------------------

# eine Variable die auffängt ob eine Taste gedrückt wurde
gedrueckt = pygame.key.get_pressed()

# bei der spieler Klasse eine richtungs liste einbauen
# rauf, runter, rechts, links
richtg = [0,0,0,0]
# je nach modell muss man verändern zb: stehen extra


# Eine geschwindigkeit Variable das sich der Spieler auch bewegen kann
geschw = 5

#----------Spieler Klasse---------

def bewegen(self):
        if self.richtg[0]:
            self.y -= self.geschw
        if self.richtg[1]:
            self.y += self.geschw
        if self.richtg[2]:
            self.x += self.geschw
        if self.richtg[3]:
            self.x -= self.geschw


#-----------In der Spiel Schleife--------------------

    gedrueckt = pygame.key.get_pressed()
    if gedrueckt[pygame.K_UP]:
        spieler1.richtg = [1,0,0,0]
    elif gedrueckt[pygame.K_DOWN]:
        spieler1.richtg = [0,1,0,0]
    elif gedrueckt[pygame.K_RIGHT]:
        spieler1.richtg = [0,0,1,0]
    elif gedrueckt[pygame.K_LEFT]:
        spieler1.richtg = [0,0,0,1]
    else:
        spieler1.richtg = [0,0,0,0]