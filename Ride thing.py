print("It iz time to select ur ride.")
print("1. Bike")
print("2. Car")

choice = int(input("Enter ur choice: "))

if( choice == 1 ):
    print("Wot type of bike???")
    print("1. Scooty (bruh)")
    print("2. Scooter (BRUUUUUH)")

    choice2 = int(input("Enter ur choice no.2: "))

    if choice2==1:
        print("U HAVE SELECTED DA SCOOTY.")
    else:
        print("U HAVE SELECTED DA SCOOTER.")

elif( choice == 2):
    print("Wot type of car???")
    print("1. Sedan")
    print("2. SUV")

    choice2 = int(input("Enter ur choice no.2: "))

    if choice2==1:
        print("U have selected a sedan.")
    else:
        print("U have selected a SUV.")