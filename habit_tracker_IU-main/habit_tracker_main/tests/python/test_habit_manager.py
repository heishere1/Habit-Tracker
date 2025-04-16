import unittest
from datetime import date
from src.python.modules.habit_manager import HabitManager

class TestHabitManager(unittest.TestCase):
    def setUp(self):
        self.manager = HabitManager()
        self.manager.add_habit("Exercise", "Health", "daily")

    def test_add_habit(self):
        habits = self.manager.list_habits()
        self.assertTrue(any("Exercise" in h for h in habits))

    def test_remove_habit(self):
        self.manager.remove_habit("Exercise")
        habits = self.manager.list_habits()
        self.assertFalse(any("Exercise" in h for h in habits))

    def test_check_in(self):
        habit = self.manager.get_habit("Exercise")
        habit.check_in(date(2024, 1, 1))
        habit.check_in(date(2024, 1, 2))
        self.assertEqual(habit.get_streak(), 2)

if __name__ == '__main__':
    unittest.main()
