# 1 - Perform a task
# 2 - Return a value

# Schlechtere Alternative -> printed den Wert auf jeden Fall
def greet(name):
    print(f"Hi {name}")

print(greet("John"))
# Besser -> Mehr Flexibilität, weil wir bekommen nur einen Wert zurück und können entscheiden ob printen, etc.
#def get_greeting(name):
#    return f"Hi {name}"

#message = get_greeting("John")
#file = open("content.txt", "w")
#file.write(message)
