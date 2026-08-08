b1 = {"apple", "banana", "mango", "apple", "grape"}
b2 = {"mango", "kiwi", "banana", "kiwi"}
print(f"Da first basket has {b1}.")
print(f"Da second basket has {b2}.")

b1.add("orange")
print(f"Da first basket after adding an orange has {b1}")

common = b1.intersection(b2)
print(f"Da fruits in both baskets are {common}.")

import array as arr
count1 = arr.array('i', [3, 5, 2, 4])
print(f"Da fruit count array contains {count1}.")

count1.insert(0, 1)
count1.append(6)
print(f"Da fruit count array iz after adding some items iz {count1}.")

count4 = count1.count(4)
print(f"Da number of times 4 appears iz {count4}.")

count1.reverse()
print(f"Da fruit count array in reverse iz {count1}.")