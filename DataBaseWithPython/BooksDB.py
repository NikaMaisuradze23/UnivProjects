import sqlite3

conn = sqlite3.connect('db_books.sqlite')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE books
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  title VARCHAR(50),
#                  author VARCHAR(100),
#                  price FLOAT);''')

# a_title = "kacia adamiani"
# a_author = "Ilia chavchavadze"
# a_pr = 8

# book_list = [
#             ('The Book Thief', 'Markus Zusak', 17 ),
#             ('Animal Farm', 'George Orwell', 13 ),
#             ('The Hunger Games', 'Suzanne Collins', 17 ),
#             ('Harry Potter and the Prisoner of Azkaban', 'Rowling',  25),
#             ('Harry Potter and the Goblet of Fire', 'Rowling', 24 ),
#             ('გამზრდელი', 'აკაკი წერეთელი', 8),
#             ('ჩემი თავგადასავალი', 'აკაკი წერეთელი', 8),
#             ('განდეგილი', 'ილია ჭავჭავაძე', 10)]
#
# cursor.executemany("INSERT INTO books (title, author, price) VALUES (?,?,?)", book_list)
# conn.commit()

cursor.execute("SELECT * FROM books")
record = cursor.fetchmany(4)

for row in record:
    print(row)





conn.close()