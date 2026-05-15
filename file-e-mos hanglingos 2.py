import os
print("CHECK IF junk mo tunk.txt FILE EXISTS OR NOT OR IM COOKED")
if os.path.exists("my_file."):
    os.remove("my_file")
else:
    print("im dead oh no i can fix dat")

my_file = open("junk mo tunk.txt", 'w')
my_file.write("gam gamitos gam gamitosi gam gamitos gam gamitos gam gamitos gam gamitos")
my_file.close()