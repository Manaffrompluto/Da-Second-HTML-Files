import random
import math
print("Da random module helps Python chose  values randomly.")
play = True
num = str(random.randint(1, 8))
print("Now a random number from 1 to 8 will be printed and u guess it.")

while play:
    guess = input("Enter da selected number from 1 to 8: ")
    if num == guess:
        print("U guessed it!!!")
        print("Now math ceil, floor, copysign, fabs and gcd calculations.")
        print("A ceil value rounds a number up to da nearest whole integer while da floor value does di opposite.")
        print('For example, 26.7 equals to ' + str(math.ceil(26.7)) + ' ceil value, while it equals to ' + str(math.floor(26.7)) + ' floor value.')
        print("A copysign value takes da size of da first number and gives it da mathematical sign (+ or -) of da second number.")
        x = 15
        y = -20
        print('e.g. da x value(15) after copying da sign from y(-20) equals to ' + str(math.copysign(x, y)) + '.')
        print("Fabs returns the absolute value of a number, which is always positive.")
        print('e.g. -7.6 equals to ' + str(math.fabs(-7.6)) + ' fabs value.')
        print("A gcd value finds da largest integer dat can perfectly divide two or more numbers without leaving a remainder.")
        print('e.g. da gcd of 11 and 24 iz ' + str(math.gcd(11)) + ' and ' + str(math.gcd(24)) + '.')
        break
    else:
        print("Incorrect, try again!")
    