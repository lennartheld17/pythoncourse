#Keyword arguments - kwargs

def increment(number, by):
    return number + by

#result = increment(2, 1)
#print(result)

#print(increment(2, 1)) #kompaktere Schreibweise. Zwischenergebnis wird in Zwischenvar. gespeichert

print(increment(2, by=1)) #by=1 -> keyword argument, um die Lesbarkeit zu erhöhen