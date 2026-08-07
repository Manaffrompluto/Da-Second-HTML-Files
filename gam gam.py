data = {
    "id1": {"name": "Idiot", "class": "IV", "subjects": "Math, English, Science"},
    "id2": {"name": "gam gam", "class": "IV", "subjects": "Math, English, Science"},
    "id3": {"name": "Chom chom", "class": "IV", "subjects": "Math, English, Science"},
    "id4": {"name": "Stoopid", "class": "V", "subjects": "Math, English, Science"},
}

result = {}
key = []

for id, details in data.items():
    key2 = (details["name"], details["class"], details["subjects"])

    if key2 not in key:
        key.append(key2)
        result[id] = details

for k, v in result.items():
    print(k, ":", v)