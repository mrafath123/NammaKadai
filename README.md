# Namma Kadai - Purchase/Sales Management Web Application

**Namma Kadai** is a web application designed for managing inventory, purchases, and sales for a small shop. Built using Flask, this application includes basic inventory tracking, financial transactions, and real-time updates of stock levels and cash balance.

## Project Structure

NammaKadai/
│
├── app/                           # Main application folder
│   ├── __init__.py                # Initializes Flask app and database
│   ├── models.py                  # Defines database models (Company, Item, Purchase, Sales)
│   ├── routes.py                  # Defines application routes for main functionalities
│   ├── config.py                  # (Optional) Configuration settings
│   └── templates/                 # HTML templates for the application
│       ├── index.html             # Homepage template showing cash balance and items
│       ├── items.html             # Template for adding new items
│       ├── purchases.html         # Template for adding purchase entries
│       └── sales.html             # Template for adding sales entries
├── run.py                         # Main script to run the application
└── store.db                       # SQLite database file (created on first run)


### Screenshots
Home page
![Home page](https://github.com/user-attachments/assets/855e74d9-e3da-48fb-900f-77b6ebc4a349)
Add items page
![Add items page](https://github.com/user-attachments/assets/5ad6af81-85db-4e70-97a4-0d380fb8287b)
Purchase items page
![Purchase items page](https://github.com/user-attachments/assets/7a7c134c-7990-44ae-9c3c-933643c9dc05)
sales item page
![sales item page](https://github.com/user-attachments/assets/edf3907d-055b-4782-94d6-8edcb54498c7)

### Features

- Inventory Management: Add, view, and manage items in inventory.
- Purchases: Record purchases, updating item quantities and cash balance.
- Sales: Log sales transactions, adjusting item quantities and cash balance.
- Real-Time Balance Display: Displays current cash balance and item stock levels on the homepage.



### Installation and Setup

Prerequisites
- Python 3.x and Git installed on your system.

Clone the Repository

git clone https://github.com/mrafath123/NammaKadai.git
cd NammaKadai

Create a Virtual Environment

python -m venv venv

Activate the virtual environment:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

Or manually install necessary packages:

pip install Flask Flask-SQLAlchemy

### Database Setup
Run the app to initialize the database and add initial data.

python run.py

This creates store.db in the root folder, which is an SQLite database storing inventory, purchase, and sales data.

### Running the Application
To start the web server,
run:

python run.py

Access the application at http://127.0.0.1:5000/.

### Project Files
app/__init__.py: Sets up the Flask application and initializes the database.
app/models.py: Contains database models for the application, including Company, Item, Purchase, and Sales.
app/routes.py: Defines routes for managing items, purchases, and sales.
run.py: Main entry point to start the application.
HTML Templates: Rendered with dynamic data using Flask templates and styled with CSS for a modern look.

### Usage
Homepage (index.html): Displays current cash balance and available items with quantities.
Add Item (items.html): Allows adding new items to inventory.
Add Purchase (purchases.html): Records a purchase, increasing item quantity and reducing cash balance.
Add Sale (sales.html): Logs a sale, decreasing item quantity and increasing cash balance.





