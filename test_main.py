import unittest
import pytest
from unittest.mock import patch
import main
class TestMain(unittest.TestCase):
# Test Option 1: Habit selection
    def test_main_option_1(self):
        with patch("main.get_db"), \
             patch("main.register_or_login"), \
             patch("main.main_menu", return_value=1), \
             patch("main.get_int_choice", return_value=1), \
             patch("main.predefined_habits"), \
             patch("main.prompt_for_periodicity"), \
             patch("main.prompt_for_end_date"), \
             patch("main.get_all_habits"), \
             patch("main.return_to_menu") as mock_return:
            main.run_main()
            mock_return.assert_called_once()

# Test Option 2: display active habits
    def test_main_option_2(self):
        with patch("main.get_db"), \
             patch("main.register_or_login"), \
             patch("main.main_menu", return_value=2), \
             patch("main.get_all_habits"), \
             patch("main.return_to_menu") as mock_return:
            main.run_main()
            mock_return.assert_called_once()

# Test Option 3: Habits update
    def test_main_option_3(self):
        with patch("main.get_db"), \
            patch("main.register_or_login"), \
            patch("main.main_menu", return_value=3), \
            patch("main.get_all_habits"), \
            patch("main.get_int_choice", return_value=1), \
            patch("main.prompt_update_habit"), \
            patch("main.return_to_menu") as mock_return:
            main.run_main()
            mock_return.assert_called_once()

# Test Option 4: Habit mark complete
    def test_main_option_4(self):
        with patch("main.get_db") as mock_get_db, \
            patch("main.register_or_login"), \
            patch("main.main_menu", return_value=4), \
            patch("main.get_all_habits"), \
            patch("main.get_int_choice", side_effect=[1, 1]), \
            patch("main.db.get_habit_ids", return_value=[1]), \
            patch("main.task_periodicity", return_value=("Take 10000 steps", "daily")), \
            patch("main.return_to_menu") as mock_return:
            main.run_main()
            mock_return.assert_called_once()

# Test option 5: delete a Habit 
    def test_main_option_5(self):
        with patch("main.get_db") as mock_get_db, \
            patch("main.register_or_login"), \
            patch("main.main_menu", return_value=5), \
            patch("main.get_all_habits"), \
            patch("main.prompt_for_habit_id", return_value=1), \
            patch("main.get_int_choice", return_value=1), \
            patch("main.db.get_habit_ids", return_value=[1]), \
            patch("main.task_periodicity", return_value=("Take 10000 steps", "daily")), \
            patch("main.db.delete_habit"), \
            patch("main.return_to_menu") as mock_return:
            main.run_main()
            mock_return.assert_called_once()

# Test Option 6: analyse
    def test_main_option_6(self):
        with patch("main.get_db"), \
            patch("main.register_or_login"), \
            patch("main.main_menu", return_value=6), \
            patch("main.get_int_choice", return_value=1), \
            patch("main.get_all_habits"), \
            patch("main.return_to_menu") as mock_return:
            main.run_main()
            mock_return.assert_not_called()

    # Test unvalid option
    def test_main_invalid_option(self):
        with patch("main.get_db"), \
            patch("main.register_or_login"), \
            patch("main.main_menu", return_value=999), \
            patch("main.return_to_menu") as mock_return:
            main.run_main()
            mock_return.assert_called_once()
if __name__ == "__main__":
    unittest.main()