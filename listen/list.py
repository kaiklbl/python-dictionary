# in einer Liste kannst du Werte verändern und austauschen

thisList = ["Harlad","Peter","rudi"]

print(thisList)             #printed die ganze Liste

print(len(thisList))        # gibt die länge von der Liste zurück

# in einer Liste können alle Datentypen gespeichert werden auch gemischt

print(type(thisList))       # gibt als typ list zurück

myList = list(("Hansi", "Klausi", "mua", 2, 6,7,2))      # andere Art um Liste zu machen

print(myList[1])          # fangen mit index 0 an 1 ist also das zweite Element

print(myList[-2])         # wird rückwerts gezält doch hier bei 1 anfangen

print(myList[2:5])        # gibt eine Liste zurück von index 2/ 3/ und 4
                        #wenn man die vordere Zahl wegglässt fängt man bei 0 an
                        # mit - Zahlen zählt es von hinten an


if "Hansi" in myList:       # schauen ob bestimmter Wert in der Liste vorhanden
    print("suppa")


myList[1] = "Mustafa"       #so ändert man Werte

myList.insert(4,"Mitsubishi")       # gibt ein Neues Element in das Array nach der stelle Was man angibt

myList.append("Flasche")        # fügt ein neues Element am schluss der Liste ein

# myList.extend(anderListe)      ==      würde zwei Sachen miteinander Verbinden miteinander kombinieren

myList.remove("Mustafa")        # entfernt das Element was man angibt aus der Liste
print(myList)

myList.pop(1)           # entfernt den Index was man angibt aus der Liste 
print(myList)

myList.pop()            # ohne angabe entfern es das letzte Element
print(myList)

del myList[1]            # entfernt den Index was man angibt aus der Liste
print(myList)           # wenn man ohne [] schreibt löscht es die ganze Liste

myList.clear()          # löscht alle Elemente aus Liste aber die Liste selbst bleibt bestehen
print(myList)

List = [8,4,3,2,6,4,8,6,2,1,29]

List.sort()                      # sortiert die Liste auch Buchstaben nach alphabet


List.reverse()       # sortiert von groß nach klein


liste2 = List.copy()        # koppiert eine Liste auf eine andere






