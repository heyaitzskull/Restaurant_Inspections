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

**Clone the repository:** <br>
git clone <repository_url><br>
cd RestaurantInspections/Inspections

**Create a virtual environment and install dependencies:** <br>
python -m venv venv<br>
venv\Scripts\activate (On Mac: source venv/bin/activate)<br>
pip install -r requirements.txt OR pip install django

**Apply migrations and run the server:** <br>
python manage.py migrate<br>
python manage.py runserver<br>

## Homepage


**With only name**
<img width="3839" height="1856" alt="image" src="https://github.com/user-attachments/assets/81ca2878-6c8d-47d1-80b3-fc3bd4b769d1" />

**With name and address**
<img width="3840" height="1862" alt="image" src="https://github.com/user-attachments/assets/290d574c-a4bc-4124-9bfa-d6e053ecfec9" />

## Search Restaurant
<img width="3840" height="1866" alt="image" src="https://github.com/user-attachments/assets/7739170f-8cd0-4f9b-88ed-a8b3b5d84c2f" />

## Restaurant Inspection Details
<img width="3840" height="1867" alt="image" src="https://github.com/user-attachments/assets/bbe8067e-262c-49b3-b62f-e1ba57cc0297" />

**Map**
<img width="3840" height="1867" alt="image" src="https://github.com/user-attachments/assets/a21c16cf-7049-4d01-a9ea-caec8c94669c" />

<img width="3840" height="1868" alt="image" src="https://github.com/user-attachments/assets/2f37e4e3-1a5b-4499-9bfc-23a40643e9d1" />

