# Alle Variablen z.B. course sind Objekte in Python
# Mit . kann man auf die Methoden (Funktionen) der Objekte zugreifen z.B. course.lower
# ACHTUNG: GROß- UND KLEINSCHREIBUNG BEACHTEN!)

course = "  python programming"
print(course.upper()) # -> Alles in Großbuchstaben konvertieren
print(course.lower()) # -> Alles in Kleinbuchstaben konvertieren
print(course.title()) # -> Die Wörter groß schreiben
print(course.rstrip()) # -> Leerzeichen am Anfang werden entfernt
print(course.find("Pro")) # -> "Bei welchem Index beginnt das Wort "Pro"?
print(course.replace("p","j")) # -> Den Buchstabe "p" durch "j" ersetzen
print("pro" in course) # -> Ist der Teil "pro" in der Variable "course" enthalten? -> BOOL
print("swift" not in course) # -> Ist der Teil "swift" nicht in der Variable "course" enthalten? -> BOOL

