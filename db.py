from psycopg2 import pool

try:
    connection_pool = pool.SimpleConnectionPool(
        1,  # min number of connections
        10, # max number of connections
        dbname="therapist",
        user="postgres",
        password="talha7640",
        host="localhost",
        port="5432"
    )
    if connection_pool:
        print("Connection pool created successfully")
        
except Exception as e:
    print("Error while connecting to PostgreSQL", e)

def get_connection():
    return connection_pool.getconn()

def release_connection(conn):
    connection_pool.putconn(conn)

def close_all_connections():
    connection_pool.closeall()

