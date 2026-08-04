import random
import math
print("Da random module helps Python chose values randomly.")
play = True
num = str(random.randint(0, 10))
print("Now a random number from 0 to 10 will be printed and u guess it.")

while play:
    guess = input("Enter da selected number from 1 to 10: ")
    if num == guess:
        print("U guessed it!!!")
        print("Now stinky math stuff.")
        option = input("Do u wanna learn about ceil and floor, copysign, fabs, or gcd (Optional): ")
        if option == "ceil and floor" or option == "Ceil and Floor" or option == "Ceil and floor" or option == "Ceil And Floor" or option == "Ceil" or option == "ceil" or option == "Floor" or option == "floor":
            print("A ceil value rounds a number up to da nearest whole integer while da floor value does di opposite.")
            print('For example, 26.7 equals to ' + str(math.ceil(26.7)) + ' ceil value, while it equals to ' + str(math.floor(26.7)) + ' floor value.')
            break

        elif option == "Copysign" or option == "copysign":
            print("A copysign value takes da size of da first number and gives it da mathematical sign (+ or -) of da second number.")
            x = 15
            y = -20
            print('e.g. da x value(15) after copying da sign from y(-20) equals to ' + str(math.copysign(x, y)) + '.')
            break

        elif option == "Fabs" or option == "fabs":
            print("Fabs returns the absolute value of a number, which is always positive.")
            print('e.g. -7.6 equals to ' + str(math.fabs(-7.6)) + ' fabs value.')
            break

        elif option == "Gcd" or option == "gcd": 
            print("A gcd value finds da largest integer dat can perfectly divide two or more numbers without leaving a remainder.")
            print('e.g. da gcd of 11 and 24 iz ' + str(math.gcd(11)) + ' and ' + str(math.gcd(24)) + '.')
            break

        else:
            print("Oh! I guess u don't wanna learn. Seriously, WHO WANTS TO LEARN MATH")
            break
    else:
        print("Incorrect, try again!")
