while True:
    try:
        bill = int(input("Enter 180 coins as ur house bill (Can be exchanged if u entered too much): "))
    
        if (bill == 180):
            print("U have cleared ur house bills!")
            break
        elif (bill < 180):
            print("Add more!\n")
        elif (bill > 180):
            print(f"Entered more than needed! Ur exchange iz {bill - 180} bucks. Have cleared ur house bills!")
            break
        
    except ValueError:
        print("Enter only da bill amount!\n")
