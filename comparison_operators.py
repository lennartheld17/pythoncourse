a = 10 > 3
b = 10 >= 3
c = 10 < 3
d = 10 <= 3
e = 10 == 3
f = 10 != 3 # Ungleich
g = 10 == "10" # False, weil untersch. Datentypen

#print(a, b, c, d, e, f, g)

h = "bag" > "apple" # True, weil "bag" in alphabetischer Reihenfolge nach "apple" kommt
i = "bag" == "BAG" # False, weil Case Sensitive
print(h, i)
