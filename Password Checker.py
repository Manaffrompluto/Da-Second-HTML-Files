import re

user = input("Enter a password: ")

def password(password_str):
    score = 0
    if re.search(r"[A-Z]", password_str) is not None:
        score += 1
    if re.search(r"[a-z]", password_str) is not None:
        score += 1
    if len(password_str) >= 8:
        score += 1
    if re.search(r"[0-9]", password_str) is not None:
        score += 1
    if re.search(r"[!@#$%&*^]", password_str) is not None:
        score += 1

    if score >= 5:
        print("Da password strength iz strong :)")
    elif score >= 3:
        print("Da password strength iz moderate. Consider adding a few more elements :)")
    else:
        print("Da password iz weak :(")
    
password(user)   