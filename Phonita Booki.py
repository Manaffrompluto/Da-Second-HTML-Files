import sys

def initial_phonebook():
    rows, cols = int(input("Enter da initial number of contacts (idk why): ")), 5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in da following order ONLY OR ELSE: " % (i+1))
        print("Note: * indicates MANDOTORY FIELDS WHICH ARE VERY BERRILY MANDATORY")
        
print("..............................................................")
temp = []
for j in range:
    if j == 0:
        temp.append(str(input("Enter ur Name*: ")))

        if temp[j] == '' or if temp[j] == ' ':
            sys.exit("NAME IS A FREAKING MANDATORY FIELD FILL IT OR JUST EXIT GRR")

    if j == 1:
        temp.append(int(input("Enter ur number*: ")))
        
    if j == 2:
        temp.append(int(input("Enter ur email address(not mandatory has there is no *): ")))
            
        if temp[j] == '' or if temp[j] == ' ':
            temp[j] = None

    if j == 3:
        
