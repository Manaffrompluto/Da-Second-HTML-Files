def add(P, Q):
    return P + Q
def substract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q

print("choose from any one of these operations:")
print("a. Add")
print("b. Substract")
print("c. Multiply")
print("d. Divide.")

choice = input("enter ur choice (a/b/c/d): ")

num_1 = int(input("Now enter da first number of the operation: "))
num_2 = int(input("Now the second number: "))

if choice == 'a':
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':
    print(num_1, " - ", num_2, " = ", substract(num_1, num_2))

elif choice == 'c':
    print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))

else:
    print("Dis is an invalid input.")
