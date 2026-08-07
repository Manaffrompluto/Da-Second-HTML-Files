print("Quiz project!!!")
print("There will be 5 questions, try to ans all of em!!!")
print("Also, to make it harder, if u make a mistake, u restart all over again!")
play = True
attempt = 1

while play:
    print(f"Attempt {attempt}")
    guess = input("What iz da best selling console of all time?: ")
    if guess == 'PS2' or guess == 'ps2':
        print("Correct! Next question.")
        guess1 = input("Wot iz da largest water body?: ")
        if guess1 == 'Pacific' or guess1 == 'pacific':
            print("Correct! Next question!")
            guess2 = input("Wot iz Spiderman's real name?: ")
            if guess2 == 'Peter parker' or guess2 == 'Peter Parker' or guess2 == 'peter parker':
                print("Correct! Next question.")
                guess3 = input("Wot was da first time period of Earth?: ")
                if guess3 == 'Hadean Eon' or guess3 == 'Hadean eon' or guess3 == 'hadean eon':
                    print("Correct! Last question.")
                    guess4 = input("Wot was da most terrifying dinosaur?: ")
                    if guess4 == 'Tyrannosaurus' or guess4 == 'tyrannosaurus':
                        print("Correct! U win!!!")
                        if attempt == 1:
                            print(f"It took ya {attempt} attempt!")
                        else:
                            print(f"It took ya {attempt} attempts!")
                        break

                    else:
                        print("Incorrect! Restart!")
                        attempt += 1
                else:
                    print("Incorrect! Restart!")
                    attempt += 1
            else:
                print("Incorrect! Restart!")
                attempt += 1
        else:
            print("Incorrect! Restart!")
            attempt += 1
    else:
        print("Incorrect! Try again!")  
        attempt += 1            
