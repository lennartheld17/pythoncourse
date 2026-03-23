#xargs - Für Funktionen, bei denen die Anzahl der Argumente veränderlich sein soll

#def multiply(x,y):
#    return x * y

#multiply(2, 3, 4 ,5) #das klappt nicht, da mehr Argumente vorgegeben als die Funktion kennt

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))