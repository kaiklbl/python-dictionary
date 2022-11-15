# Sets sind nicht geordnet und können  verändert werden

mySet = {"Hansi", "hat", "keinen", "Bock"}          # Sets werden mit {} geschrieben

print(mySet)        # gibt immer in irgendeiner Reihenfolge aus

print(len(mySet))             # gibt länge zurück

print(type(mySet))            # gibt Datentyp zurück

print("banana" in mySet)      # gibt einen boolischen Wert zurück

mySet.add('bananana')           # fügt ein neues Element hinzu

mySet.remove("Hansi")           # entfernt das Element wenn es aber nicht gibt ist FEHLER

mySet.discard("hat")            # entfernt das Element wenn es aber nicht gibt ist trotzdem kein Fehler

mySet.pop()             # entfernt letztes Element

# del mySet         ==      Löscht ganzes Set

# mySet.clear()     ==      löscht alle Elemente aus mySet





