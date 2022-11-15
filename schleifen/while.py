# -----------------while Schleife --------------

i = 1               # eine Variable fürs Zählen

while i < 5:            # Die while Schleife führt so lange aus bis die Bedingung erfüllt ist
    print(i)
    i += 1              # hier wird die ZählVariable plus 1 gerechnet bei jedn Durchlauf
                        # sonst wäre es eine Endlosschleife und das Programm stürzt ab


a = 1

while a < 6:
    print(a)
    if a == 3:
        break              # mit break kann mans auch abbrechen wenn if Bedingung erfüllt ist
    a += 1                 # bei continue (statt break) würde er nur den einen Durchlauf auslassen


