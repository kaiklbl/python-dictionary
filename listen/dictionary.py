# Dictionarys speichert einträge mit    key: value pairs
# es dürfen darin keine doppelten Sachen vorkommen


thisdict = {                # geht auch in einer Zeile aber wegen lesbarkeit
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))             # gibt länge zurück  key:value pairs zählen als eines

print(type(thisdict))            # gibt Datentyp zurück

print(thisdict.get("model"))      # gibt den wert von modell zurück also Mustang

print(thisdict.keys())            # gibt eine Liste von den Key Werten zurück

thisdict["color"] = "white"     # fügt neuen key:value pair wert hinzu

print(thisdict.values())        # gibt values zurück

print(thisdict.items())        # gibt alle Werte einzeln in Tuples zurück

thisdict["color"] = "red"       # verändert einen Wert

thisdict.pop("model")           # entfernt ein Element wenn in () leer ist gibt er einen Fehler zurück

thisdict.popitem()              # entfernt das letzte Element

# del thisdict      ==      löscht es komplett

#thisdict.clear()   ==      löscht alle Einträge

print(thisdict)

#---------- Man kann auch Dictionarys in Dictionarys machen-------

newDict = {'super':1}

thisdict.update(newDict)

print(thisdict)