tuple = [1, 0, 0, 1, 0, 1, 1]
print(tuple)
print("This is a tuple.")

try:
    something = 1
    something += 1 or something == 1
    if something == 2:
        print(f"This uses f function. Var something value: {something}")
    else:
        print("Since something value didnt go up to 2, pass value iz used.")
        pass
    
except ValueError:
    print("This iz da except error function in use.")