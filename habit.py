
from datetime import datetime, timedelta

from db import get_db, update_habit

class Habit:
    predefined_habits={
        "1": "Take 10000 steps",
        "2": "Hobby activity",
        "3": "Avoid juice and alcohol",
        "4": "Monitor weight",
        "5": "Drink 2-3L water"}
    def __init__(self, habit_id, periodicity, end_date_str=None):
        if habit_id not in self.predefined_habits:
            raise ValueError("Invalid habit ID. Please choose a number from 1 to 5.")
        if periodicity not in ["daily", "weekly"]:
            raise ValueError("Periodicity must be 'daily' or 'weekly'.")
        self.habit_id = habit_id
        self.task = Habit.predefined_habits[habit_id]
        self.task = self.predefined_habits[habit_id]
        self.periodicity = periodicity
        self.date_created = datetime.now().date()

        if end_date_str:
            try:
                self.end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("End date must be in YYYY-MM-DD format.")
            if self.end_date <= self.date_created:
                raise ValueError("End date must be after the creation date.")
        else:
            self.end_date = self.date_created + timedelta(weeks=4)

        self.checkoffs = []
def prompt_for_habit_id():
    try:
        habit_id = int(input("Enter the habit id and press enter: "))
        return habit_id
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def prompt_for_periodicity():
    print("Choose a periodicity for the habit:")
    print("Press 1 for daily")
    print("Press 2 for weekly")
    choice = input("Then press Enter: ").strip()
    if choice == '1':
        return 'daily'
    elif choice == '2':
        return 'weekly'
    else:
        print("Invalid input. Please try again.\n")
    return Habit.prompt_for_periodicity()
def prompt_for_end_date():
        print("Choose an end date for the habit:")
        while True:
            entry = input("End date (YYYY-MM-DD) or press Enter for 4 weeks from now: ").strip()
            if not entry:
                return (datetime.now().date() + timedelta(weeks=4)).isoformat()
            try:
                dt = datetime.strptime(entry, "%Y-%m-%d").date()
                if dt > datetime.now().date():
                    return dt.isoformat()
                else:
                    print("End date must be in the future.")
            except ValueError:
                print("Invalid format. Please use YYYY-MM-DD.")
def prompt_update_habit():
    db = get_db()

    try:
        habit_id = int(input("confirm the habit ID you want to update: "))
        periodicity = input("Enter new periodicity (daily or weekly): ").strip().lower()
        end_date_str = input("Enter new end date (YYYY-MM-DD): ").strip()

        update_habit(db, habit_id, periodicity, end_date_str)

    except ValueError:
        print("Please enter valid integers for user ID and habit ID.")

def mark_complete(self):
        today = datetime.now().date()
        if today > self.end_date:
            print(f"The habit period has ended on {self.end_date}. No more check-ins allowed.")
            return
        if today not in self.checkoffs:
            self.checkoffs.append(today)
            print(f"Habit '{self.task}' marked as completed on {today}.")
        else:
            print(f"Habit '{self.task}' was already completed today.")

