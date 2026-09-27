import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "customers.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    age INTEGER
)
""")


def show_menu():
    print("1. Add Customer")
    print("2. View Customer")
    print("3. Search Customer")
    print("4. Delete Customer")
    print("5. Update Customer")
    print("6. Exit")


def add_customer():
    customer_name = input("Enter your name: ")
    customer_email = input("Enter your email: ")
    customer_age = input("Enter your age: ")

    customer = {
        "name": customer_name,
        "email": customer_email,
        "age": customer_age
    }

    add_user.append(customer)

    cursor.execute(
        "INSERT INTO customers (name, email, age) VALUES (?, ?, ?)",
        (customer_name, customer_email, customer_age)
    )

    conn.commit()


print("ChatBot: Hello. Type exit to leave.")

add_user = []

while True:
    show_menu()

    user_input = input("you: ")

    if user_input.lower() == "1":
        add_customer()

    elif user_input.lower() == "2":
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        for customer in customers:
            print(customer[1])
            print(customer[2])
            print(customer[3])

    elif user_input.lower() == "3":
        search_name = input("Enter customer name to search: ")
        cursor.execute(
            "SELECT * FROM customers WHERE name = ?",
            (search_name,)
        )
        customer = cursor.fetchone()

        if customer:
            print(customer[1])
            print(customer[2])
            print(customer[3])
        else:
            print("Customer Not Found")


    elif user_input.lower() == "4":
        delete_name = input("Enter customer name to delete: ")
        cursor.execute(
            "DELETE FROM customers WHERE name = ?",
            (delete_name,)
        )
        conn.commit()

        if cursor.rowcount > 0:
            print("Customer info deleted")
        else:
            print("Customer Not Found")

    elif user_input.lower() == "5":
        update_name = input("Enter customer name to update: ")
        new_email = input("Enter new email: ")
        cursor.execute(
            "UPDATE customers SET email = ? WHERE name = ?",
            (new_email, update_name)
        )
        conn.commit()
        if cursor.rowcount > 0:
            print("Customer Updated")
        else:
            print("Customer Not Found")
    

    elif user_input.lower() == "6":
        print("ChatBot: Goodbye!")
        break

    else:
        print("Invalid Choice")