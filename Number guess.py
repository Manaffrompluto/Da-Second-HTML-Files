import random
playing = True
num = str(random.randint(0, 99))
print("A random number will be generated from 0 to 99, and u have to guess it.")

while playing:
    guess = input("Wot iz da number?: \n")
    if num == guess:
        print("Correct.")
        break

    else:
        print("Wrong. TRY AGAIN.")
    