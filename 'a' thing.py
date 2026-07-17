a = input("Enter a word: ")
flag=0

for i in a:
    if (i == 'A'):
        print("A iz found.")
        flag==1
        break
if flag==0:
    print("A iz not found.")