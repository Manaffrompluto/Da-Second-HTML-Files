num = input("Enter anything with/without numbers: ")
found = False
for i in num:
    if (i == '0') or (i == '1') or (i == '2') or (i == '3') or (i == '4') or (i == '5') or (i == '6') or (i == '7') or (i == '8') or (i == '9'):
        found = True 

if found:
    print("Numbers have been found in di input.")
else:
    print("No number has been found in di input.")