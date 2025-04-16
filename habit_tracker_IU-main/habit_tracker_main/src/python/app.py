from src.python.modules.habit_manager import HabitManager

def main():
    manager = HabitManager()

    while True:
        print("\nHABIT TRACKER CLI")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Check-in Habit")
        print("4. Remove Habit")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Habit name: ")
            category = input("Category: ")
            frequency = input("Frequency (daily/weekly/custom): ")
            manager.add_habit(name, category, frequency)

        elif choice == "2":
            habits = manager.list_habits()
            if not habits:
                print("No habits added yet.")
            else:
                for h in habits:
                    print("-", h)

        elif choice == "3":
            name = input("Enter habit to check-in: ")
            habit = manager.get_habit(name)
            if habit:
                habit.check_in()
                print("Check-in recorded.")
            else:
                print("Habit not found.")

        elif choice == "4":
            name = input("Habit to remove: ")
            manager.remove_habit(name)
            print("Removed if existed.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
