# importieren von pygame
import pygame
import sys

# pygame initialisieren
pygame.init()

# eine Variable die die screen breite und höhe beschreibt
screen = pygame.display.set_mode([x.breite,y.hoehe])

#um ein Bild zu laden
pygame.image.load('Bild')

# um auf Bildschirm was hinzuzufügen
screen.blit()

# um Hintergrund einzufärben
screen.fill((rgbwerte))

# Bildschirm updaten
pygame.display.update()

# Das ist der spielname was oben steht
pygame.display.set_caption('mein erstes spiel')

# um eine Feld um ein Objekt zu machen wegen Kollisionen
pygame.Rect(x,y,breite,hoehe)

# Kollisions Befehl
objekt.colliderect(anderesObjekt)

# um einen Sound zu laden
pygame.mixer.Sound('SoundDatei')

# um Sound abzuspielen
pygame.mixer.Sound.play(SoundVar)

# um FrameRate variable zu erstellen
clock = pygame.time.Clock()

# mit wie vielen fps es gehen soll
clock.tick(60)

#ein Rechteck zeichen Farbe in rgb werten/ letztes ist ob es gefüllt sein soll oder nicht
pygame.draw.rect(screen,farbe,(x,y,breite,hoehe),0 oder 1)


#------------------Spiel Schleife--------------------
# eine Variable festlegen für die Spielschleife
go = True

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # hier ist die SpielSchleife 
    # dakommen die funktionen und methoden rein