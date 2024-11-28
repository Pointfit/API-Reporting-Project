import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# Database Configuration
DB_CONFIG = {
    'dbname': os.getenv("DB_NAME"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': os.getenv("DB_PORT")
}

def insert_patents():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Load cleaned data
        df = pd.read_csv("cleaned_patents.csv")

        # Insert data into the database
        for _, row in df.iterrows():
            cursor.execute("""
            INSERT INTO Patents (ID, PatentNumber, Title, Abstract, Category, Subcategory, NASACenter, ImageURL, Score)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (ID) DO NOTHING;
            """, (
                row["ID"],
                row["Patent Number"],
                row["Title"],
                row["Abstract"],
                row["Category"],
                row["Subcategory"],
                row["NASA Center"],
                row["Image URL"],
                row["Score"]
            ))

        # Commit the changes
        conn.commit()
        print("Patent data inserted into the database successfully!")

    except Exception as e:
        print(f"Error inserting data into the database: {e}")

    finally:
        cursor.close()
        conn.close()

# Run the function
insert_patents()
