# Alle Variablen in Python sind nur pointer das heißt die Werte sind auch noch im Hintergrund
# da Selbst wenn man die Variable überschreibt 

myList = [[1,2],[3,4],5]

myList2 = myList            # zeigt nur auf myList

myList3 = myList[:]         # koppiert nur die Liste

# myList2[2] = 'haha'        verändert für myList und myList2
# myList3[2] = 'haha'       verändert nur für myList3


# myList[0][1] = 99           # da verändert es sich bei jedem weil das nur koppien von Wegweißern sind
# myList2[0][1] = 99
# myList3[0][1] = 99

print(myList)
print(myList2)
print(myList3)