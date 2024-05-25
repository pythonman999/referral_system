import random
import string
import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create Users table
        try:
            self.cursor.execute('''
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER UNIQUE NOT NULL,
                    referrer_id INTEGER
                );
            ''')
        except Exception:
            pass
    
    def get_user(self, user_id):
        res = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id, )).fetchall()
        # print(res)
        if len(res) == 0:
            return False
        return True
    
    def update_data(self, user_id, referrer_id = None):
        # print(referrer_id)
        with self.connection:
            if referrer_id != None:
                self.cursor.execute("INSERT INTO `users` (`user_id`, `referrer_id`) VALUES (?, ?)", (user_id, referrer_id))
            else:
                self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

            self.connection.commit()
        

    def count_referrals(self, user_id):
        res = self.cursor.execute("SELECT * FROM `users` WHERE `referrer_id` = ?", (user_id,)).fetchall()
        return len(res)
    
# Пример использования
db = Database('db/database.db')
# print(db.check_country(5444484801))
# print(db.sender_prem_users())
# print(db.sender_all_users())
