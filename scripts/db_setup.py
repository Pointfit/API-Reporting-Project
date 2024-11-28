import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def setup_database_logic():
    """Sets up the PostgreSQL database and creates necessary tables."""
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conn.cursor()

        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Materials (
            MaterialID SERIAL PRIMARY KEY,
            Name TEXT NOT NULL,
            Type TEXT
        );

        CREATE TABLE IF NOT EXISTS Properties (
            PropertyID SERIAL PRIMARY KEY,
            MaterialID INTEGER NOT NULL,
            PropertyName TEXT,
            Value REAL,
            FOREIGN KEY (MaterialID) REFERENCES Materials (MaterialID)
        );

        CREATE TABLE IF NOT EXISTS Applications (
            ApplicationID SERIAL PRIMARY KEY,
            MaterialID INTEGER NOT NULL,
            ApplicationName TEXT,
            FOREIGN KEY (MaterialID) REFERENCES Materials (MaterialID)
        );
        """)

        conn.commit()
        print("Database setup complete!")

    except Exception as e:
        print(f"Error during database setup: {e}")
    finally:
        cursor.close()
        conn.close()
