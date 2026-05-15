with open('M:/Python/TEXTITOS MATITOS.txt', 'w')as file:
  file.write("HELLO IM GAAAAAAAAAAAAAAY. ALSO U ARE. FAT.")
file.close()

with open('M:/Python/TEXTITOS MATITOS.txt', 'r')as file:
  data = file.readlines()
  print("WORDIES IN DIS FILE AREEE ")
  for line in data:
    word = line.split()
    print (word)
file.close()