from datetime import datetime
import sqlite3

from sympy import periodicity #create a database using sqlite3
#from habit import Habit 



#db = sqlite3.connect("main.db")
def get_db(name="main.db"):     #Create a database connection to the SQLite database specified by name
	db = sqlite3.connect(name)
	create_tables(db)
	return db

def create_tables(db):
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS users(
		    username TEXT PRIMARY KEY,
		    user_id INTEGER NOT NULL,
		    description TEXT)""")
	# Checkoffs-Tabelle mit user_id
	cursor.execute("""CREATE TABLE IF NOT EXISTS checkoffs (
		checkoff_id INTEGER PRIMARY KEY AUTOINCREMENT,
		user_id INTEGER NOT NULL,
		habit_id INTEGER,
		checkedoff_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (habit_id) REFERENCES habits(habit_id))""")
	
    # Streaks-Tabelle mit user_id
	cursor.execute("""CREATE TABLE IF NOT EXISTS streaks (
		streak_id INTEGER PRIMARY KEY AUTOINCREMENT,
		user_id INTEGER NOT NULL,
		habit_id INTEGER,
		started_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		ended_on DATE DEFAULT NULL,
		current_streak INTEGER DEFAULT 0,
		is_active INTEGER DEFAULT 1,
		FOREIGN KEY(habit_id) REFERENCES habits(habit_id));""")
	
	
	# Habits-Tabelle mit user_id
	cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
		habit_id INTEGER PRIMARY KEY AUTOINCREMENT,
		user_id INTEGER NOT NULL,
		task TEXT NOT NULL,
		periodicity TEXT NOT NULL,
		created_on TEXT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		updated_on TEXT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		deleted_on DATE NULL,
        end_date_str DATA NULL,
		is_active BOOLEAN DEFAULT 1)""")
	
	db.commit()
	

# Functions to interact with /add values to h habits table
def add_user(db, username):
    """
    Add a new user to the database.
    """
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
    
    db.commit()

def update_habit(conn, habit_id, periodicity, end_date_str):
    with conn:
        conn.execute("""
            UPDATE habits
            SET periodicity = ?, end_date_str = ?, updated_on = date('now')
            WHERE habit_id = ?;
        """, (periodicity, end_date_str, habit_id))
        
def delete_habit(db, user_id, habit_id):
    cur = db.cursor()
    cur.execute("""
        UPDATE habits
        SET deleted_on = date('now'), is_active = 0
        WHERE habit_id = ? AND user_id = ?; """, (habit_id, user_id))
    db.commit()

def add_checkoff(db, user_id, habit_id):
    cur = db.cursor()
    cur.execute("""
        INSERT INTO checkoffs (user_id, habit_id)
        VALUES (?, ?)""", (user_id, habit_id))
    db.commit()

def last_checkedoff_on(db, user_id, habit_id):
    cur = db.cursor()
    cur.execute("""
        SELECT checkedoff_on
        FROM checkoffs
        WHERE habit_id = ? AND user_id = ?
        ORDER BY checkedoff_on DESC
        LIMIT 1;""", (habit_id, user_id))
    return cur.fetchone()

def get_all_habits(conn):
    #return a list of all currently tracked active habits.
    cursor = conn.cursor() 
    cursor.execute("""
        SELECT habit_id, task, periodicity, end_date_str
        FROM habits
        WHERE is_active = 1
        ORDER BY habit_id;
    """)
    habits = cursor.fetchall()
    
    if not habits:
        print("No active habits found.")
        return

    print("\nActive Habits:")
    for habit in habits:
        habit_id, task, periodicity, end_date_str = habit
        print(f"ID: {habit_id} | Task: {task} | Periodicity: {periodicity} | End Date: {end_date_str}")

def get_habit_details(db, habit_id, is_active):
	cursor = db.cursor()
	cursor.execute("""
        SELECT habit_id, task, periodicity, created_on, is_active from habits where habit_id = ? and is_active = ?; """, (habit_id, is_active))
	return cursor.fetchone()

def get_habit_ids(db, is_active):
    cursor = db.cursor()
    cursor.execute("""SELECT habit_id FROM habits WHERE is_active = ?;""", (is_active,))
    return [row[0] for row in cursor.fetchall()]
def get_habits_by_periodicity(conn, user_id, periodicity, is_active):
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM habits
        WHERE user_id = ? AND periodicity = ? AND is_active = ?
    """, (user_id, periodicity, is_active))
    return cur.fetchall()
    
def start_streak(db, user_id, habit_id):
    cur = db.cursor()
    cur.execute("""
        INSERT INTO streaks (user_id, habit_id, started_on)
        VALUES (?, ?, date('now'));
    """, (user_id, habit_id))
    db.commit()

def increment_current_streak(db, user_id, habit_id):
    cur = db.cursor()
    cur.execute("""
         UPDATE streaks
         SET current_streak = current_streak + 1
         WHERE habit_id = ? AND user_id = ? AND is_active = 1;
    """, (habit_id, user_id))
    db.commit()

def end_streak(db, user_id, habit_id):
    cur = db.cursor()
    cur.execute("""
        UPDATE streaks
        SET is_active = 0, ended_on = date('now')
         WHERE habit_id = ? AND user_id = ? AND is_active = 1;
      """, (habit_id, user_id))
    db.commit()
def get_longest_streak_one_habit(db, user_id, habit_id, is_checked_off_today):
    """
    Updates the streak status depending on today's checkoff.
    If the habit was done today, increment or start a streak.
    If it was missed, end the streak.
    Then return the longest streak.
    """
    if is_checked_off_today:
        # First, try to increment existing streak
        increment_current_streak(db, user_id, habit_id)

        # Optionally check if there's no active streak and create a new one
        cur = db.cursor()
        cur.execute("""
            SELECT COUNT(*) FROM streaks
            WHERE user_id = ? AND habit_id = ? AND is_active = 1
        """, (user_id, habit_id))
        active_streak = cur.fetchone()[0]

        if active_streak == 0:
            start_streak(db, user_id, habit_id)
    else:
        # End the streak if not checked off
        end_streak(db, user_id, habit_id)

    # Finally, return the longest streak
    return get_longest_streak_one_habit(db, habit_id, is_active=1)
    print("Longest streak for this habit:", longest_streak)


	


	


          

