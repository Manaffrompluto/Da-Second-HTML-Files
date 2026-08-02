tuple1 = ('Reading', 1, 0, 0, 1, 0, 1, 1)
tuple2 = ('Excercise', 0, 0, 0, 1, 1, 0, 1)
habit = (tuple1, tuple2)
print("Habit checker.")

for week_tuple in habit:
    name = week_tuple[0]
    day_data = week_tuple[1:]
    complete_days = day_data.count(1)
    total_days = len(day_data)
    print(f"Habit: {name}.")
    print(f"{complete_days} days completed out of {total_days} days.\n")