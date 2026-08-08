data = {
    "id1": {"name": "Stoopid", "class": "III", "grade": "D"},
    "id2": {"name": "Stinky", "class": "IV", "grade": "F"},
    "id3": {"name": "Hmm", "class": "II", "grade":"C"},
}
print("Record: ")
print(data)

data["id4"] = data.get("id4", {"name": "guy", "class": "I", "grade": "B"})
print(data)

huh = len(data)
print("Data length: ")
print(huh)