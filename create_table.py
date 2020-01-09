import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text UNIQUE, email text UNIQUE, age INTEGER, password text, location text, option_1 text, option_2 text, option_3 text, option_4 text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, name text PRIMARY KEY, price real)"
cursor.execute(create_table)

connection.commit()

connection.close()
