#--------------lambda-----------------
# lambda sind kleine funktionen

x = lambda a: a + 10    # kuzSchreibweiße für einfache funktionen

print(x(20))

y = lambda a,b: a + b + 10  #können so viele Argumente haben wie man braucht

print(y(2,4))       # braucht aber dann auch 2 Argumente


def myFunk(n):
    return lambda a: a * n

mal2 = myFunk(2)            # n wird auf 2 gesetzt
mal3 = myFunk(3)            # n wird auf 3 gesetzt

print(mal2(6))              # a wird auf 6 gesetzt
print(mal3(6))

