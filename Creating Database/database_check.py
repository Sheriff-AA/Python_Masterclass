import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Enter a name: ")

# for row in conn.execute("select * from contacts where name = ?", (name,)):
for row in conn.execute("select * from contacts where name like ?", (name,)):
    print(row)

conn.close()
