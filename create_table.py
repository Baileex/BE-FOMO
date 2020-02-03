import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text UNIQUE, password text, email text UNIQUE, age text, location text, option_1 text, option_2 text, option_3 text, option_4 text, family BOOLEAN DEFAULT false, gender text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS businesses (id INTEGER PRIMARY KEY, username text UNIQUE, password text, email text UNIQUE, business_name text, address text, description text, url text, avatar text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, event_name text, name text, address text, cityname text, postcode text, longitude text, latitude text,description text, event_type text, date Date, doorsopen Time, doorsclose Time,  minage text, entryprice text, business_id INTEGER, url text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS event_history (id INTEGER PRIMARY KEY, age TEXT, sex TEXT, event_type TEXT, location TEXT, time TEXT)"
cursor.execute(create_table)

connection.commit()

connection.close()
