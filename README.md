# TechStore - E-commerce Platform

A modern, full-stack e-commerce website for tech products built with Django and styled with a sleek black and purple theme.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Product Catalog**: Browse 60+ tech products across 10 categories
- **Advanced Filtering**: Search, filter by category, and sort products
- **Shopping Cart**: Add, update, and remove items from cart
- **Checkout System**: Complete orders with automatic stock management
- **Admin Orders Page**: View all orders with statistics (staff only)
- **Responsive Design**: Modern UI with black and purple theme
- **Admin Panel**: Full admin access for product and order management

## Tech Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite
- **Frontend**: Bootstrap 5, Font Awesome
- **Forms**: Django Crispy Forms

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Setup Instructions

1. **Clone or navigate to the project directory**

2. **Run the setup script** (Linux/Mac):
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Or manually install** (Windows/All platforms):
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run migrations
   python manage.py makemigrations
   python manage.py migrate
   
   # Populate database with products and categories
   python manage.py populate_db
   
   # Add product images
   python manage.py add_images
   
   # Create test users (optional)
   python manage.py create_test_users
   ```

4. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the application**:
   - Main site: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

## Default Credentials

### Admin User
- **Username**: admin
- **Password**: admin123

### Test Users (if created)
- **Customer 1**: john / password123
- **Customer 2**: jane / password123
- **Staff User**: staff / password123

## Usage

### For Customers
1. Register a new account or login
2. Browse products on the home page or products page
3. Use filters and search to find specific items
4. View product details
5. Add items to cart (requires login)
6. Review cart and update quantities
7. Checkout to complete order

### For Admins
1. Login to admin panel at `/admin`
2. Manage categories, products, orders
3. View customer information
4. Update product stock and pricing

## Project Structure

```
techstore/
├── manage.py
├── requirements.txt
├── setup.sh
├── techstore/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── shop/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── context_processors.py
│   └── management/
│       └── commands/
│           └── populate_db.py
└── templates/
    ├── base.html
    └── shop/
        ├── home.html
        ├── product_list.html
        ├── product_detail.html
        ├── cart.html
        ├── login.html
        └── register.html
```

## Product Categories

- Laptops
- Desktops
- Monitors
- Keyboards
- Mice
- Headphones
- Webcams
- Speakers
- Graphics Cards
- Processors

## Features in Detail

### Authentication
- Users must register/login to add items to cart
- Guest users can browse products
- Secure password validation

### Shopping Cart
- Persistent cart per user
- Real-time quantity updates
- Stock validation
- Subtotal calculations

### Product Management
- 60+ pre-loaded products
- Category-based organization
- Stock tracking
- Price management
- Product images from Unsplash

### Checkout
- Order creation with items
- Automatic stock deduction
- Order history tracking
- Redirect to home after successful checkout

## Customization

### Adding Products
Use the admin panel or create a custom management command to add more products.

### Styling
Modify the CSS variables in `templates/base.html` to change the color scheme:
```css
:root {
    --primary-purple: #8b5cf6;
    --dark-purple: #6d28d9;
    --bg-dark: #0f0f0f;
    /* ... */
}
```

## License

This project is for educational purposes.

## Support

For issues or questions, please check the Django documentation at https://docs.djangoproject.com/
