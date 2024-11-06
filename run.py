from app import create_app, db
from app.models import init_data

# Create the app instance
app = create_app()

# Initialize data (company, items)
with app.app_context():
    db.create_all()  # Create tables
    init_data()  # Initialize the database with company and items

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
