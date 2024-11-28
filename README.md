# API Reporting Project

## Overview
This project demonstrates an end-to-end data pipeline that:
1. Fetches data from the NASA TechTransfer API.
2. Processes and cleans the data.
3. Inserts the data into a PostgreSQL database.
4. Generates insightful visualizations to analyze patents.

## Key Features
- Full pipeline automation from API data fetch to visualizations.
- Data analysis and visualization:
  - Patents by NASA center.
  - Top subcategories of patents.
  - Distribution of patent scores.
  - Word cloud of patent titles.

## Technologies Used
- **Languages:** Python, SQL
- **Database:** PostgreSQL
- **Libraries:** pandas, matplotlib, SQLAlchemy, WordCloud

## Setup Instructions
1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/api-reporting-project.git
   cd api-reporting-project
   ```
   
2. **Install dependencies:**
   Ensure you have Python 3.8+ and PostgreSQL installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Set up PostgreSQL:**
- Create a database named materials_project.
- Use the table schema provided in scripts/insert_patents.py to set up the database.

4. **Run the pipeline: Fetch, clean, and insert the data into PostgreSQL:**
   ```bash
   python scripts/patent_pipeline.py
   ```
   
5. **Generate visualizations: Produce visual insights and save them to the visualizations folder:**
   ```bash
   python scripts/visualization.py
   ```