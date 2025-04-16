from src.python.modules.habit import Habit

class HabitManager:
    def __init__(self):
        self.habits = []

    def add_habit(self, name, category, frequency):
        new_habit = Habit(name, category, frequency)
        self.habits.append(new_habit)

    def remove_habit(self, name):
        self.habits = [h for h in self.habits if h.name != name]

    def get_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def list_habits(self):
        return [str(habit) for habit in self.habits]
