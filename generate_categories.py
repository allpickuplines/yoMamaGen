import sqlite3
import re

categories = []

db_connection = sqlite3.connect('yomama.db')
db = db_connection.cursor()

db.execute('DROP TABLE IF EXISTS categories')
db.execute('''CREATE TABLE IF NOT EXISTS categories 
            (id INTEGER NOT NULL PRIMARY KEY, 
            category TEXT NOT NULL, 
            quantity INTEGER)''')

for row in db.execute('''SELECT DISTINCT categories
                        FROM jokes'''):
    categories.append(row)

for category in categories:
    db.execute('''SELECT count(1) FROM jokes 
                WHERE categories = ?''', category)
    category  = str(category).replace("(u'", '').replace("',)", '')
    quantity = str(db.fetchone()).replace('(', '').replace(',)', '')
    params = [(str(category)), (str(quantity))]
    with db_connection:
        db.execute('''INSERT INTO categories (category, quantity)
                    VALUES (?, ?)''', params)