import unittest
from datetime import datetime, timedelta
from habit import Habit

class TestHabit(unittest.TestCase):

    def test_valid_initialization_with_default_end_date(self):
        today = datetime.now().date()
        habit = Habit("1", "daily")
        expected_end = today + timedelta(weeks=4)

        self.assertEqual(habit.task, "Take 10000 steps")
        self.assertEqual(habit.periodicity, "daily")
        self.assertEqual(habit.date_created, today)
        self.assertEqual(habit.end_date, expected_end)
        self.assertEqual(habit.checkoffs, [])

    def test_valid_initialization_with_custom_end_date(self):
        today = datetime.now().date()
        future_date = (today + timedelta(days=10)).strftime("%Y-%m-%d")
        habit = Habit("2", "weekly", future_date)
        expected_end = datetime.strptime(future_date, "%Y-%m-%d").date()
        self.assertEqual(habit.end_date, expected_end)

    def test_invalid_habit_id(self):
        with self.assertRaises(ValueError):
            Habit("6", "daily")

    def test_invalid_periodicity(self):
        with self.assertRaises(ValueError):
            Habit("1", "monthly")

    def test_invalid_end_date_format(self):
        with self.assertRaises(ValueError):
            Habit("1", "daily", "20-05-2025")

    def test_end_date_before_creation(self):
        past_date = (datetime.now().date() - timedelta(days=1)).strftime("%Y-%m-%d")
        with self.assertRaises(ValueError):
            Habit("1", "daily", past_date)

if __name__ == "__main__":
    unittest.main()