high_income = True
good_credit = True
student = True

if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

#if not student: #not-Operator -> if not student heißt: wenn student False ist, dann wird print("Eligible") ausgeführt
    #print("Eligible")
#else:
    #print("Not Eligible")