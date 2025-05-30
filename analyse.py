
import db
from db import get_all_habits, get_db, get_habits_by_periodicity, get_longest_streak_one_habit

conn = db.get_db()
is_active = True


class Analysis:
    def __init__(self, conn, user_id, habit_id, is_checked_off_today):
        self.conn = conn
        self.user_id = user_id
        self.habit_id = habit_id
        self.is_checked_off_today = is_checked_off_today

        get_all_habits(conn) 
        db.get_habits_by_periodicity(conn, user_id, 'daily', True)
        db.get_habits_by_periodicity(conn, user_id, 'weekly', True)

        get_longest_streak_one_habit(conn, user_id, habit_id, is_checked_off_today)

