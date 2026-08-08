yummy = {"Popcorn", "Chicken Drum", "Burger", "Chips"}
healthy = {"Apple", "Banana", "Carrot", "Spinach"}

print(f"Da yummy snacks are {yummy}.")
print(f"Da healthy snacks are {healthy}.")

healthy.add("Orange")
print(f"Da healthy snacks list after adding a fruit iz {healthy}.")

import array as arr
c = arr.array('i', [4])
e = arr.array('i', [4])
print(f"Da full snacks array iz {c + e}.")

l = list(yummy)
l.reverse()
print(f"Da yummy snacks array in reverse are {l}.")

l1 = list(healthy)
l1.reverse()
print(f"Da healthy snacks array in reverse are {l1}.")
