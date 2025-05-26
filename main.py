#from typing import Self
from db import get_db, get_habits_by_periodicity, get_longest_streak_one_habit, get_all_habits, update_habit
import db
from functions_main import main_menu, register_or_login, get_int_choice, return_to_menu, task_periodicity, predefined_habits
from habit import prompt_for_habit_id, prompt_for_periodicity, prompt_for_end_date, prompt_update_habit
def run_main():
    conn = db.get_db()
    active_habits = db.get_habit_ids(conn, 1) 

    register_or_login()

    # Main program:
    user_choice = main_menu()

    if user_choice == 1:
        print("\n Please enter the habit ID to select a habit from the list:")
        print(predefined_habits())
        habit_id = get_int_choice()
        prompt_for_periodicity()
        prompt_for_end_date()
        conn = get_db()
        get_all_habits(conn)
        return_to_menu()

    elif user_choice == 2:
        print("Here is a list of your active habits \n")
        conn = get_db()
        get_all_habits(conn)    
        return_to_menu()

    elif user_choice == 3:
        print("You chose to update a habit. Here are your current habits:\n")
        conn = get_db()
        get_all_habits(conn)
        print("\n Which habit would you like to update? Enter the habit id and press enter:")
        habit_id = get_int_choice()
        prompt_update_habit()
        #active_habits = db.get_habit_ids(db, is_active=1)
        return_to_menu()
        print("\n your habit has been successfully update")
    elif user_choice == 4:
        print("\n You chose to mark a habit as completed. Here are your current habits:")
        conn = get_db()
        get_all_habits(conn)
        print("\n Which habit would you like to mark as completed? Enter the habit id and press enter:")
        habit_id = get_int_choice()
        conn = db.get_db()  # assuming get_db() returns the connection
        active_habits = db.get_habit_ids(conn, 1)

        if not active_habits:
            print("No active habits found.")
        else:
            if habit_id in active_habits:
                task_name, periodicity = task_periodicity(conn, habit_id, 'user', 1)
                print(f"You chose to mark habit {habit_id}, {task_name} as completed. The periodicity is {periodicity}. Are you sure? Enter 1 for yes, 2 for no")
                choice = get_int_choice()

                if choice == 1:
                    print(f"Well done. Your streak is still active. Habit {habit_id} marked as completed.\n")
                elif choice == 2:
                    print("Habit completion not updated.")
                else:
                    print("Invalid input. Please enter 1 for yes, 2 for no.")
            else:
                print("Invalid input. Please enter a valid habit id.")
        return_to_menu()

    elif user_choice == 5:
        print("You chose to delete a habit. Here are your current habits:")
        get_all_habits(db, is_active=1)

        habit_id = prompt_for_habit_id()  # ✅ Capture return value
        if habit_id is None:
            print("Deletion cancelled due to invalid habit id.")
            return_to_menu()

        conn = db.get_db()
        active_habits = db.get_habit_ids(conn, 1)

        if habit_id in active_habits:
            task_name, periodicity = task_periodicity(conn, habit_id, 1)
            print(f"You chose to delete habit {habit_id}, {task_name}. The periodicity is {periodicity}. Are you sure? Enter 1 for yes, 2 for no")
            choice = get_int_choice()

            if choice == 1:
                db.delete_habit(conn, habit_id)
                print(f"Habit {habit_id} deleted successfully!\n")
            elif choice == 2:
                print("Habit not deleted.")
            else:
                print("Invalid input. Please enter 1 for yes, 2 for no.")
        else:
            print("Invalid input. Please enter a valid habit id.")

        return_to_menu()

    elif user_choice == 6:
        print("Let's see how you are doing. What would you like to analyze?")
        print("1. get_all_tracked_habits")
        print("2. get_habits_by_periodicity")
        print("3. get_longest_streak_for_habit")
        choice = get_int_choice()
        if choice == 1:
            get_all_habits()

        elif choice == 2:
            get_habits_by_periodicity()

        elif choice == 3:
            get_longest_streak_one_habit()

    else:
        print("Invalid input. Please enter a valid option number.")
        return_to_menu()

if __name__ == "__main__":
    run_main()

        