import os
import subprocess
from db_setup import *
from fetch_patents import fetch_patent_data, process_patent_data
from insert_patents import insert_patents
from visualization import plot_patents_by_center, plot_top_subcategories, plot_patent_scores, plot_wordcloud

def setup_database():
    """Set up the PostgreSQL database and tables."""
    print("\n=== Step 1: Setting up the database ===")
    try:
        setup_database_logic()
        print("Database setup completed successfully.")
    except Exception as e:
        print(f"Database setup failed: {e}")

def fetch_and_clean_data():
    """Fetch data from NASA API and clean it."""
    print("\n=== Step 2: Fetching and cleaning data ===")
    try:
        raw_data = fetch_patent_data()
        if raw_data:
            cleaned_data = process_patent_data(raw_data)
            print("Data fetched and cleaned successfully.")
        else:
            print("Failed to fetch data.")
    except Exception as e:
        print(f"Data fetching/cleaning failed: {e}")

def insert_data_into_db():
    """Insert cleaned data into PostgreSQL."""
    print("\n=== Step 3: Inserting data into PostgreSQL ===")
    try:
        insert_patents()
        print("Data inserted into PostgreSQL successfully.")
    except Exception as e:
        print(f"Data insertion failed: {e}")

def generate_visualizations():
    """Generate visualizations from PostgreSQL data."""
    print("\n=== Step 4: Generating visualizations ===")
    try:
        plot_patents_by_center()
        plot_top_subcategories()
        plot_patent_scores()
        plot_wordcloud()
        print("Visualizations generated successfully.")
    except Exception as e:
        print(f"Visualization generation failed: {e}")

if __name__ == "__main__":
    setup_database()
    fetch_and_clean_data()
    insert_data_into_db()
    generate_visualizations()
