# The functions defined here will be used in the main.py file.
import sys
import sqlite3
from analyse import Analysis
import db
from db import get_db

def register_or_login():
    print("Welcome to the application!\n")
    username = input("Enter your username: ").strip()
    conn = db.get_db()
    
    try:
        db.add_user(conn, username)
        print(f"User '{username}' registered successfully.")
    except sqlite3.IntegrityError:
        print(f"Welcome back, {username}!")
    
def predefined_habits():
    return {
        "1": "Take 10000 steps",
        "2": "Hobby activity",
        "3": "Avoid juice and alcohol",
        "4": "Monitor weight",
        "5": "Drink 2-3L water"}

def main_menu():
    print("What would you like to do?")
    print("1. select your habits")
    print("2. View your habits")
    print("3. Update a habit")
    print("4. Mark a habit as completed")
    print("5. Delete a habit")
    print("6. Analyze your habits")
    print("7. Quit the program")
    print("What would you like to do next? Type the number of your choice please. ")
    while True:
        choice = input()
        try:
            int_choice = int(choice)
            if 1 <= int_choice <= 7:
                if int_choice == 7:
                    sys.exit("Thank you for using the application. Goodbye!")
                return int_choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid option number.")

def get_int_choice(): #Function to prompt the user for an integer input
    
        choice = input()
        try:
            int_choice = int(choice)

            if int_choice == 1:
                print(" you choose to take 10000 steps")
            elif int_choice == 2:
                print("you choose a hobby activity")
            elif int_choice == 3:
                print("you choose to avoid juice and alcohol")
            elif int_choice == 4: 
                print("you choose to monitor weight")
            elif int_choice == 5: 
                print("you choose to drink 2-3L water")           
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid option number.")

def return_to_menu(): #prompt the user to press Enter to return to the main menu
    input("Press Enter to return to the main menu...")
    main_menu()

#def get_all_habits(self, db, is_active): #Function to display the list of habits retrieved from the database
   # analysis_habit_list = Analysis()
    #analysis_habit_list.get_all_habits(db, 1)

def task_periodicity(db, habit_id, is_active):
    task, periodicity = task_periodicity.get_task_periodicity(db, habit_id, is_active)
    return task, periodicity