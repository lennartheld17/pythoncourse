successful = True

for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break #Aus dem for-loop herausgehen, wenn der Code ausgeführt wurde
else:
    print("Attempted 3 times and failed!")