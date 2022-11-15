# ein funktion ist ein code Block den man immer wieder aufrufen kann
# wird in python mit def geschrieben

def myFunk():               # zuerst def dann funktionsname
    print("Hello Bobios")   # dann code Block was es ausführen soll

myFunk()                    # so ruft man funktion auf



def myName(name):           # funktion mit Arguments / Argumente ist egal wie der heißt
    print("hello " + name)

myName("Hansi")             # wir wird das Argument übergeben
myName("Jonny")



def fullName(fname,lname):  # kann so viele argumente haben wie du willst 
    print(fname)
    print(lname)

fullName("hansi","hineter")   # es müssen dann immer 2 argumente übergeben werden sonstt Fehler


#---------------------------------------------------------------
#falls man nicht weiß wie viele argumente es übergeben werden kommt ein * beim argument
# es hat sich als name *args durchgesetzt


def myKids(*args):      # die argumente werden dann zu einem tuple
    print(args)

myKids("H","A","E")     # so viel übergeben wie man will


#----------------------------------------------------------------------
# falls man ein dictionary braucht und man weiß die einGaben nicht kommen zwei **
# es hat sich als name **kwargs durchgesetzt


def mykid(**kwargs):        # da kommt ein dictionary raus
    print(kwargs)

mykid(fname = "Hauer",lname = "Bauer")      # man muss key: value pairs übergeben sonst Fehler


#--------------------------------------------------------------
# default Parameter Value

def whichCountry(country = "Belgien"):     # Parameter bekommt einen Wert 
    print(country)                          # der wird nur genommen falls nichts übergeben wird


whichCountry("italien")
whichCountry()                      # hier kommt Belgien


#--------------------------------------------------------------
# return Werte

def mal(zahl):            # return gibt den Programm etwas zurück
    return zahl*5

print(mal(6))

def irgendwas():
    pass            # pass ist nur platzhalter das man später weitermachen kann

# funktionen können als argumente positional,optional mit default wert, *args, **kwargs

def wasmachtreturn():
    return                  # entweder returnd 0, None, oder False
