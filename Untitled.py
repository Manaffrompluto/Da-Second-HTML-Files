def factorial(x):

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("Da factorial of 0 iz",factorial(0))
print("Da factorial of 1 iz",factorial(1))
print("Da factorial of 2 iz",factorial(2))
print("Da factorial of 5 iz",factorial(5))
print("Da factorial of 10 iz",factorial(10))
