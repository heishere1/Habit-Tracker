import csv
habits = []
while True:
    habit_name = input("Enter your habit (or  'q' to quit): ").strip()
    if habit_name.lower() == 'q' :
        break
    habits.append(habit_name)
with open('habit.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
writer.writerow(['Habit Name'])