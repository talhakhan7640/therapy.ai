from db import get_connection, release_connection

# store users into db
def insert_therapist(firstName, lastName, email, password, gender):
    conn = get_connection() 
    cur = conn.cursor()

    try:
        cur.execute (
            "INSERT INTO users(firstName, lastName, email, password, gender) VALUES (%s, %s, %s, %s, %s)",
        (firstName, lastName, email, password, gender)
    )
        conn.commit()
    except Exception as e:
        print("Error executing query", e)
        conn.rollback()
    finally:
        cur.close()
        release_connection(conn)
