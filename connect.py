import psycopg2
from decouple import config


def connect():
    conn = None

    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(
            database=config("DB_NAME"),
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            host=config("DB_HOST"),
            port=config("DB_PORT"),
        )

        # create a cursor
        curr = conn.cursor()

        # execute a statement
        curr.execute("SELECT version();")

        # display the PostgreSQL database server version
        db_version = curr.fetchone()
        print("DB RETURN : " + str(db_version))

        # close db connection
        curr.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed")


if __name__ == "__main__":
    connect()
