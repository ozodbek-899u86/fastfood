#
# import sqlite3
#
# db = sqlite3.connect('database.sqlite')
# cursor = db.cursor()
#
#
#
# # cursor.execute("""SELECT * FROM users WHERE user_id = ?""", (659237008,))
# # users = cursor.fetchall()
# # print(users)
# cursor.execute("""CREATE TABLE IF NOT EXISTS users(
# user_id INTEGER PRIMARY KEY AUTOINCREMENT,
# chat_id INTEGER UNIQUE,
# adduser_id VARCHAR(100) )""")
