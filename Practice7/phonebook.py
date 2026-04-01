import psycopg2
import csv
from config import params

def connect():
    """ Connect to the PostgreSQL database server """
    return psycopg2.connect(**params)

def insert_from_csv(file_path):
    query = "INSERT INTO phonebook(first_name, last_name, phone_number) VALUES(%s, %s, %s) ON CONFLICT (phone_number) DO NOTHING;"
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                with open(file_path, mode='r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader) # Skip header
                    cur.executemany(query, list(reader))
                conn.commit()
        print("CSV imported successfully.")
    except Exception as e:
        print(f"Error: {e}")

def add_contact(fname, lname, phone):
    query = "INSERT INTO phonebook(first_name, last_name, phone_number) VALUES(%s, %s, %s);"
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fname, lname, phone))
            conn.commit()
        print("Contact added.")
    except Exception as e:
        print(f"Error: {e}")

def update_contact(user_id, new_name=None, new_phone=None):
    if new_name:
        sql = "UPDATE phonebook SET first_name = %s WHERE user_id = %s"
        val = (new_name, user_id)
    else:
        sql = "UPDATE phonebook SET phone_number = %s WHERE user_id = %s"
        val = (new_phone, user_id)
    
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, val)
        conn.commit()

def query_contacts(filter_type, value):
    if filter_type == "name":
        sql = "SELECT * FROM phonebook WHERE first_name ILIKE %s"
        val = (f"%{value}%",)
    else:
        sql = "SELECT * FROM phonebook WHERE phone_number LIKE %s"
        val = (f"{value}%",)

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, val)
            return cur.fetchall()

def delete_contact(identifier, is_phone=False):
    column = "phone_number" if is_phone else "first_name"
    sql = f"DELETE FROM phonebook WHERE {column} = %s"
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (identifier,))
        conn.commit()