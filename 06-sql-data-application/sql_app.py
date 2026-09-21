import sqlite3

connection = sqlite3.connect("customers.db")

cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT)
    """
)
cursor.execute(
    """INSERT OR IGNORE INTO customers(id, name, email)
       VALUES (?, ?, ?)
    """,
    (1, "Joseph", "Joseph@email.co")
)

connection.commit()


cursor.execute(
    """UPDATE customers
       SET email = "Joseph@gmail.com"
       WHERE id = 1
    """
)

connection.commit()

cursor.execute(
    """SELECT * FROM customers
       WHERE id = 1
    """
)

customers = cursor.fetchall()

print(customers)


cursor.execute(
   """UPDATE customers
        SET name = "Joe"
        WHERE id = 1
   """
)

connection.commit()

cursor.execute(
    """SELECT * FROM customers
       WHERE id = 1
    """
)


customers = cursor.fetchall()

print(customers)

connection.close()