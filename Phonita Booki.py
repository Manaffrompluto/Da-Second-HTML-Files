import sys

def phone_book():
    rows, cols = int(input("Enter da initial number of contacts (idk why): ")), 5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in da following order ONLY OR ELSE: " % (i+1))
        print("Note: * indicates MANDOTORY FIELDS WHICH ARE VERY BERRILY MANDATORY")
        
        print("...........................................................................")
        temp = []
        for j in range(cols):
           if j == 0:
                temp.append(str(input("Enter your Name*: ")))

                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("NAME IS A FREAKING MANDATORY FIELD FILL IT OR JUST EXIT GRR")

           if j == 1:
                temp.append(int(input("Enter your contact number*: ")))
        
           if j == 2:
                temp.append(int(input("Enter your email address: ")))
            
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

           if j == 3:
            temp.append(str(input("Enter your date of birth(mm/dd/yy): ")))
        
            if temp[j] == '' or temp[j] == ' ':
                temp[j] = None

            if j == 4:
                temp.append(str(input("Enter your category(Family/Friend/Work/Other): ")))

            if temp[j] == '' or temp[j] == ' ':
                temp[j] = None
    
        phone_book.append(temp)

    print(phone_book)
    return phone_book
       
def menu():
    print("*******************************************************************************")
    print("\t\t\Device Directory", flush=False)
    print("*******************************************************************************")
    print("\tYou can now perform the following operations on this PhoneBook\n")
    print("1. Add a new contact.")
    print("2. Remove an existing contact.")
    print("3. Delete all contacts.")
    print("4. Search for a contact.")
    print("5. Display all contacts.")
    print("6. Exit this PhoneBook.")

def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter your name: ")))
        if i == 1:
            dip.append(str(input("Enter your contact number: ")))
        if i == 2:
            dip.append(str(input("Enter your email address:")))
        if i == 3:
            dip.append(str(input("Enter your date of brith(mm/dd/yy): ")))
        if i == 4:
            dip.append(str(input("Enter your category(Family/Friend/Work/Other): ")))
    pb.append(dip)
    return pb

ch = 1
pb = phone_book()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)