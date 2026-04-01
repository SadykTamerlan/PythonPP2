import psycopg2
from config import params

def connect():
    """Connect to the PostgreSQL database server"""
    conn = None
    try:
        # Connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        # Create a cursor
        cur = conn.cursor()
        
        # Execute a statement to verify connection
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(f'PostgreSQL database version: {db_version}')
        
        # Close the communication with the PostgreSQL
        cur.close()
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    connect()