try:
    number = int(input("Pls enter ur age: "))
    if (number >= 8):
        if number % 2 == 0:
            print("Da age iz valid and itz an even number.")
        else:
            print("Da age iz valid and itz an odd number.")
    else:
        print("Da age entered iz not valid.")

except ValueError:
    print("Please only enter numbers. Try again.")