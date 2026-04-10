num = int(input("Enter a number: "))
c = 0

if num > 1:

    for i in range(1, num+1):
        if (num % i) == 0:
            c=c+1

if (c==2):
    print("This is a prime number hohoho.")
else:
    print("THis ain't a prime number bruh.")
        