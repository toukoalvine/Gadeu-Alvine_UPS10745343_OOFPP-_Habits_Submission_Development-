
import db


class Analysis:

    #def __init__(self):
        #pass

    #def get_all_habits(Self):
        #Return a list of all currently tracked (active) habits.
        #conn = db.get_db()
        #cursor = conn.cursor()
       # cursor.execute("""
           # SELECT habit_id, task, periodicity 
           # FROM habits 
           # WHERE is_active = 1
       # """)
        #results = cursor.fetchall()
        #for habit in results:
           # print(habit)

    def get_habits_by_periodicity(self, db, periodicity):
        #Return a list of all habits with the same periodicity ('daily' or 'weekly')
        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT habit_id, task 
            FROM habits 
            WHERE periodicity = ?
        """, (periodicity,))
        return cursor.fetchall()


    def get_longest_streak_for_habit(self, db, habit_id):
        #Return the longest run streak for a specific habit by ID
        cursor = db.cursor()
        cursor.execute("""
            SELECT current_streak 
            FROM streaks 
            WHERE habit_id = ?
        """, (habit_id,))
        result = cursor.fetchone()
        return result[0] if result else 0