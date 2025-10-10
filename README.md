###**Restaurant Inspections Website**

A full-stack web application that consolidates restaurant inspection data across multiple cities, providing a dynamic, searchable interface with interactive maps.

##**Technologies**
Backend: Django, SQLite
Frontend: HTML, CSS, JavaScript, Leaflet.js
Data: Restaurant inspection datasets from Chicago, NYC, and LA

##**Features**
Centralized platform combining fragmented inspection datasets
Interactive Leaflet.js maps with color-coded markers for inspection results
Search and filter restaurants by city, cuisine, or inspection score
Detailed restaurant inspection histories and violation records
ETL pipeline for migrating 400,000+ records with data cleaning, validation, and normalization

##**Installation**

Clone the repository:
git clone <repository_url>
cd restaurant-inspections

Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

##**Apply migrations and run the server:**
python manage.py migrate
python manage.py runserver

