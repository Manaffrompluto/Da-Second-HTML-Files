try:
    print("Welcome to the calculator!!!")
    print("choose from any of da 4 options: 1.Add 2.Substract 3.Multiply 4. Divide.")

    choice = input("Enter from these options: ")
    if choice == "Add" or choice == "add":
        num_1 = float(input("Enter da first number: "))
        num_2 = float(input("Enter da second number: "))
        total = num_1 + num_2
        print(f"Da sum iz {total}.")

    if choice == "Substract" or choice == "substract":
        num_1 = float(input("Enter da first number: "))
        num_2 = float(input("Enter da second number: "))
        total = num_1 - num_2
        print(f"Da minuend iz {total}.")

    if choice == "Multiply" or choice == "multiply":
        num_1 = float(input("Enter da first number: "))
        num_2 = float(input("Enter da second number: "))
        total = num_1 * num_2
        print(f"Da product iz {total}.")

    if choice == "Divide" or choice == "divide":
        num_1 = float(input("Enter da first number: "))
        num_2 = float(input("Enter da second number: "))
        total = num_1 / num_2
        print(f"Da quotient iz {total}.")

except ValueError:
    print("Enter only numbers! Run again!")

except ZeroDivisionError:
    print("Dont't divide by zero! Run again!")
