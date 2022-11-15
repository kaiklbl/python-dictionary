# die Oberhaupt ElternKlasse ist Objekt (myClass erbt von Object)


class myClass:
    classproperty = 'Klasseneigenschaft'        # gehört nur der Klasse

    def __init__(self,number):
        self.objprop = 'Objekteigenschaft'      # gehört dem objekt
        self.number = number
    
    def myMethod(self):
        return 'Hurra'

myObjekt = myClass(1)
print(myObjekt.__dict__)            # sind nur die Eigenschaften vom Objekt

