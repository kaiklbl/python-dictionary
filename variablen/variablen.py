# Rechenoperatoren
# +  plus
# -  minus
# *  mal
# /  durch 
# %  Modollu (dividiert gibt aber nur in Rest als Ergebniss zurück)

string = "hallo"        # python erkennt automatisch welcher Datentyp es ist

intiger = 10

floatNumber = 2.0  

numberAsString = str(6)         #macht aus intiger String gibt auch die Befehle int()/str()/float()

print(numberAsString)           # mit print macht man ausgabe

print(type(numberAsString))     # gibt den Datentyp zurück

x,y,z = 1,2,3           # so kann man mehrer variablen in einer Zeile anlegen

x = 3               # man kann vorhandene variablen auch überschreiben

x=y=z = "Hallo"     # mehreren Variablen den gleichen wert zuweisen

print(x,y,z)        # um mehrer variablen auszugeben man kann auch + dazwischen statt ,
                    # bei + kann man aber nicht verschiedene Datentypen verbinden


# in einer funktion kann man das keyword 'global' verwenden das die Variable auch auserhalb funkt



for i in 'banana':              # gibt die einzelnen buchstaben in jeden Schleifendurchlauf aus
    print(i)


print(len(x))               # gibt die länge aus

print('a' in x)             #sucht das gesuchte in der variable falls vorhanden gibt es True zurück


b = 'habara'

print(b[2:5])       # gibt nur die buchstaben 2,3,4 zurück 

print(b[-5:-2])     # fangt von hinten zum zählen an startindex ist immer 0

print(b.upper())     # gibt nur in großbuchstaben zurück

print(b.lower())    # gibt nur in Kleinbuchstaben zurück

print(b.replace('h', 'd'))      # ersetzt die buchstaben mit einem anderen

wort = 'Futschi, Tuschi'

print(wort.split(','))      # tut ab , Trennen in zwei einzelen strings

userInput = input("Hier kann der user was eingeben: ")
print(userInput)           # um eine userEingabe zu machen die wird dann auf die variable übernommen


#------------------Scope------------------
# Eine Variable die innerhalb einer funktion gemacht wurde gibt es auch nur in der funktion == Local Scope
# Eine Variable herausen zählt überall == Global Scope

# in einer funktion kann man eine Variable global machen mit dem Keyword -> global
# zB:  global x = 5   dann zählt x überall

