# tuples können nicht mehr verändert werden
# Sie werden mit () geschrieben

myTuple = ("Hansi", "geht", "gerne", "Gasii")       # starten bei index 0

print(len(myTuple))             # gibt länge zurück

print(type(myTuple))            # gibt Datentyp zurück

print(myTuple[1])           # gibt nur den Wert vom index zurück

print(myTuple.count("Hansi"))       # gibt an wie oft das gesuchte im Tuple ist

print(myTuple.index("Hansi"))       # gibt den Index vom Wert zurück
