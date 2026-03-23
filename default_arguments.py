# Kwargs können auch standardmäßig auf best. Wert gesetzt werden

def increment(number, by=5): #by=5 -> Festgelegtes Standard Argument
    return number + by

print(increment(2, 10)) #standard Wert wird überschrieben, wenn beim Aufrufen der Funktion ein Wert für das zweite Argument vorgegeben wird