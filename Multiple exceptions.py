try:
    num_1, num_2 = eval(input("Enter two numbers separated by a comma: "))
    result = num_1 / num_2
    print("The result is", result)

except ZeroDivisionError:
    print("Error: division by zero.")

except SyntaxError:
    print("Error: Didn't include a comma between the two numbers.")

except:
    print("Error: Wrong input.")

else:
    print("No errors found.")

finally:
    print("Run the program and follow the instructions for proper division if there's an error.")