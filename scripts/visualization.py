import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from wordcloud import WordCloud
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

# Create SQLAlchemy engine
connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
engine = create_engine(connection_string)

# Fetch data from PostgreSQL
def fetch_data(query):
    try:
        df = pd.read_sql(query, engine)  # Use SQLAlchemy engine
        print(f"Data fetched successfully for query: {query}")
        print("Columns:", df.columns)  # Debug: Print column names
        print(df.head())  # Debug: Preview the data
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Visualization 1: Pie Chart - Patents by NASA Center
def plot_patents_by_center():
    query = """
    SELECT NASACenter AS nasacenter, COUNT(*) AS totalpatents
    FROM Patents
    GROUP BY NASACenter
    ORDER BY totalpatents DESC;
    """
    df = fetch_data(query)

    # Ensure columns are named correctly
    df.columns = ['NASACenter', 'TotalPatents']

    plt.figure(figsize=(8, 8))
    plt.pie(df['TotalPatents'], labels=df['NASACenter'], autopct='%1.1f%%', startangle=140)
    plt.title('Patents by NASA Center', fontsize=16)
    plt.tight_layout()
    plt.savefig("../visualizations/patents_by_center.png")
    print("Saved: ../visualizations/patents_by_center.png")
    plt.show()

# Visualization 2: Horizontal Bar Chart - Top 5 Subcategories
def plot_top_subcategories():
    query = """
    SELECT subcategory, COUNT(*) AS totalpatents
    FROM patents
    GROUP BY subcategory
    ORDER BY totalpatents DESC
    LIMIT 5;
    """
    df = fetch_data(query)

    # Debug: Print column names to confirm casing
    print("Columns in DataFrame:", df.columns)

    # Use the correct column names as returned by the query
    plt.figure(figsize=(10, 6))
    plt.barh(df['subcategory'], df['totalpatents'], color='skyblue')  # Use lowercase here
    plt.title('Top 5 Subcategories by Patents', fontsize=16)
    plt.xlabel('Total Patents', fontsize=12)
    plt.ylabel('Subcategory', fontsize=12)
    plt.tight_layout()
    plt.savefig("../visualizations/top_subcategories.png")
    print("Saved: ../visualizations/top_subcategories.png")
    plt.show()

# Visualization 3: Scatter Plot - Patent Scores
def plot_patent_scores():
    query = "SELECT Title, Score FROM Patents WHERE Score IS NOT NULL;"
    df = fetch_data(query)

    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(df)), df['score'], color='purple', alpha=0.7)
    plt.title('Patent Scores Distribution', fontsize=16)
    plt.xlabel('Patent Index', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.tight_layout()
    plt.savefig("../visualizations/patent_scores.png")
    print("Saved: ../visualizations/patent_scores.png")
    plt.show()

# Visualization 4: Word Cloud - Keywords in Patent Titles
def plot_wordcloud():
    query = "SELECT Title FROM Patents;"
    df = fetch_data(query)

    text = " ".join(df['title'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Keywords in Patent Titles', fontsize=16)
    plt.tight_layout()
    plt.savefig("../visualizations/wordcloud_titles.png")
    print("Saved: ../visualizations/wordcloud_titles.png")
    plt.show()

# Main Function to Run All Visualizations
if __name__ == "__main__":
    plot_patents_by_center()
    plot_top_subcategories()
    plot_patent_scores()
    plot_wordcloud()
