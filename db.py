from app import app, db  # Replace 'your_app' with the name of your Flask app/module

# Ensure the application context is active
with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
