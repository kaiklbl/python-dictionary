#--------------for Schleife-------------------

# Die for Schleife wird Hauptsaechlich fuer listen/tuples/sets/dictionarys benutzt

print("Beispiel:1")

fruits = ["banana", "apfel", "gurke"]

for x in fruits:            # die for Schleife geht durch jedes Element aus der Liste durch
    print(x)                # den wert bekommt bei jeden Schleifen durchlauf x 
                            # x kann auch anders benannt werden ist egal

print("Beispiel:2")

for letters in "banana":    # wenn man nur einen String angibt bekommt man die einzelnen Buchstaben
    print(letters)


print("Beispiel:3")

for obst in fruits:
    print(obst)
    if obst == "apfel":     # wenn Ein Schleifendurchgang "apfel" ist bricht er ab
        break

print("Beispiel:4")

for obst in fruits:
    if obst == "apfel":     # wenn Ein Schleifendurchgang "apfel" ist lässt er diesen Durchgang aus
        continue
    print(obst)

print("Beispiel:5")

for abc in range(6):        # range() ist wie viele durchgänge gemacht werden solln
    print(abc)


print("Beispiel:6")

for abc in range(2,6):        # range() fangt jetzt erst bei 2 an
    print(abc)


print("Beispiel:7")

for abc in range(3,30, 6):        # range() es zählt jetzt immer in 6 Schritten 
    print(abc)                    # fängt aber bei 3 an bis 30 heißt:
                                  # 3/ 9/ 15/ 21/ 27

# break und continue kann man bei der for Schleife auch wieder

#----------------nested Loops------------------

print("Beispiel:8")

farbe = ["rote","gelbe","blaue"]
gemuese = ["Karotte","Lauch","Gurke"]

for x in farbe:
    for y in gemuese:
        print(x,y)

