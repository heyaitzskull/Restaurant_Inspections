# Restaurant Inspections Website
Created by: Prativa Khatiwada

A full-stack web application that consolidates restaurant inspection data across multiple cities, providing a dynamic, searchable interface with interactive maps.

### Technologies
Backend: Django, SQLite <br>
Frontend: HTML, CSS, JavaScript, Leaflet.js <br>
Data: Restaurant inspection datasets from Chicago, NYC, and LA <br>

###  Features
Centralized platform combining fragmented inspection datasets <br>
Interactive Leaflet.js maps with color-coded markers for inspection results<br>
Search and filter restaurants by city, cuisine, or inspection score <br>
Detailed restaurant inspection histories and violation records <br>
ETL pipeline for migrating 400,000+ records with data cleaning, validation, and normalization<br>

**Installation**

**Clone the repository:**
git clone <repository_url><br>
cd restaurant-inspections

**Create a virtual environment and install dependencies:**
python -m venv venv<br>
source venv/bin/activate  (On Windows: venv\Scripts\activate)<br>
pip install -r requirements.txt

**Apply migrations and run the server:**
python manage.py migrate<br>
python manage.py runserver<br>

