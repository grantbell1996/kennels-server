import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {   
        "id": 1,
        "name": "Bruce Dickenson",
    },
    {
        "id": 2,
        "name": "Alice Cooper"
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    # make a variable to hold the found employee
    requested_customer = None
    
    # iterate through the EMPLOYEES list
    for customer in CUSTOMERS:
        # dictionaries use [] notation to find a key on an object instead of dot notation
        if customer["id"] == id:
            requested_customer = customer
            
    return requested_customer

def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)