try:
    number = int(input("Enter a number: "))
    print("Da number entered iz", number)

except ValueError as ex:
    print("Error: ", ex)