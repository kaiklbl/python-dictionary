# classen werden immer mit class und danach der KlassenName erstellt

class Mensch:
    age = 23


print(Mensch.age)      # gibt den gespeicherte age wert von Mensch aus

hansi = Mensch()        # neues Objekt hansi wurde erstellt er hat jetzt alle Eigenschaften von Mensch
print(hansi.age)        # deswegen ist er jetzt 23 Jahre alt

# --------------------------------------------------------------------

class Person:                       # classe mit __init__ fuction
    def __init__(self,name,age):    # durch die kann man die Werte dann selbst vergeben
        self.name = name            #self braucht man um in der classe auf die Eigenen Werte zuzugreifen
        self.age = age

    def myfunk(self):                   # eine Methode die jetzt jedes Objekt von dieser Klasse benutzen kann
        print("hi I am " + self.name)




person1 = Person("Hansi",44)        # neue Person wurde angelegt mit eigenen Namen und Alter
print(person1.name)
print(person1.age)

person1.myfunk()            # aufruf einer classen Methode

person1.age = 45            # so kann man Werte wieder ändern

del person1.age             # so löscht man einzeln Elemente

del person1                 # löscht das komplette Objekt wieder


#-------------------Child Klasse-------------------
# erbt von Eltern Klasse

class Student(Person):                  # in den Klammern von wem Klasse erbt
    def __init__(self, name, age, klasse):      # müssen alle vorhandenen + neue
        super().__init__(name, age)             #super hollt von Eltern die Werte und Methoden
        self.klasse = klasse                    # Neuer Wert hinzugefügt
        self.jahrgang = 2019                    # setzt einen neuen fixen wert

    def myfunk(self):
        print("Hi i am "+ self.name + " i am a Student")    
        # polymorphismus ist wenn vererbte Methoden überschrieben werden

        

bobo = Student("bobo",26,"p777")

print(bobo.name)
print(bobo.age)
print(bobo.klasse)
print(bobo.jahrgang)
bobo.myfunk()
