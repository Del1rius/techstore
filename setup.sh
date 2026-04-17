#!/bin/bash

echo "Setting up TechStore E-commerce Platform..."

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Populate database with products and create admin user
python manage.py populate_db

echo ""
echo "Setup complete!"
echo ""
echo "Admin credentials:"
echo "  Username: admin"
echo "  Password: admin123"
echo ""
echo "To start the server, run:"
echo "  python manage.py runserver"
echo ""
echo "Then visit: http://127.0.0.1:8000"
