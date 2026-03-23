comand = ""
while True: #infinite loop -> wichtig man braucht eine break condition sonst unendlich (Überlauf!!)
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break