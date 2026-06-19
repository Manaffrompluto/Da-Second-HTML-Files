medical_cause = input("Did u have a medical cause (Y/N)?: ").strip().upper()

if medical_cause == 'Y':
    print("Ur allowed.")
else:
    atten = int(input("enter attendance of da students (wot): "))

    if atten >= 75:
        print("ALLOWED")
    else:
        print("NOT ALLOWED")
