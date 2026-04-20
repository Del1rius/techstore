# TechStore - E-commerce Platform

A modern, full-stack e-commerce website for tech products built with Django and styled with a sleek black and purple theme.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Product Catalog**: Browse 94+ tech products across 12 categories
- **Advanced Filtering**: Search, filter by category, and sort products
- **Shopping Cart**: Add, update, and remove items from cart
- **Checkout System**: Complete orders with automatic stock management
- **Admin Orders Page**: View all orders with statistics (staff only)
- **Product Specifications**: Detailed specs for all products
- **Responsive Design**: Modern UI with black and purple theme
- **Admin Panel**: Full admin access for product and order management

## Tech Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite
- **Frontend**: Bootstrap 5, Font Awesome
- **Forms**: Django Crispy Forms

## Quick Start (Recommended)

The repository includes a pre-populated database with all products, so you can get started immediately!

### Prerequisites
- Python 3.8 or higher
- pip

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Del1rius/techstore.git
   cd techstore
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the application**:
   - Main site: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

**That's it!** The database is already populated with 94 products, categories, and an admin user.

## Default Credentials

### Admin User
- **Username**: admin
- **Password**: admin123

## Alternative Setup (Fresh Database)

If you want to start with a fresh database instead of using the included one:

1. **Delete the existing database**:
   ```bash
   rm db.sqlite3  # Linux/Mac
   del db.sqlite3  # Windows
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create admin user**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Populate database with products**:
   ```bash
   python manage.py populate_db
   python manage.py add_specifications
   python manage.py add_more_products
   python manage.py update_prices_and_images
   ```

5. **Create test users (optional)**:
   ```bash
   python manage.py create_test_users
   ```

## Product Categories

- Laptops (10 products)
- Desktops (10 products)
- Monitors (10 products)
- Keyboards (5 products)
- Mice (5 products)
- Headphones (5 products)
- Webcams (5 products)
- Speakers (5 products)
- Graphics Cards (8 products)
- Processors (8 products)
- RAM (8 products)
- Motherboards (10 products)

**Total: 94 products with realistic South African Rand (R) pricing**

## Usage

### For Customers
1. Register a new account or login
2. Browse products on the home page or products page
3. Use filters and search to find specific items
4. View product details and specifications
5. Add items to cart (requires login)
6. Review cart and update quantities
7. Checkout to complete order

### For Admins
1. Login to admin panel at `/admin`
2. Manage categories, products, orders
3. View customer information
4. Update product stock and pricing
5. Access admin orders page at `/orders/` (staff only)

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
- 94 pre-loaded products with specifications
- Category-based organization
- Stock tracking
- Price management in South African Rand (R)
- Product images

### Checkout
- Order creation with items
- Automatic stock deduction
- Order history tracking
- Redirect to home after successful checkout

### Admin Orders Page
- View all orders in one place
- Order statistics (total orders, revenue, average order value)
- Expandable order details
- Staff-only access

## Project Structure

```
techstore/
├── manage.py
├── requirements.txt
├── db.sqlite3                    # Pre-populated database
├── README.md
├── techstore/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/
│   ├── models.py                 # Product, Category, Cart, Order models
│   ├── views.py                  # All view logic
│   ├── urls.py
│   ├── admin.py
│   ├── context_processors.py
│   ├── templatetags/
│   │   └── order_filters.py      # Custom template filters
│   └── management/
│       └── commands/
│           ├── populate_db.py
│           ├── add_specifications.py
│           ├── add_more_products.py
│           ├── update_prices_and_images.py
│           └── create_test_users.py
└── templates/
    ├── base.html
    └── shop/
        ├── home.html
        ├── product_list.html
        ├── product_detail.html
        ├── cart.html
        ├── login.html
        ├── register.html
        └── admin_orders.html
```

## Testing

The included database has:
- ✅ Admin user (admin/admin123)
- ✅ 94 products across 12 categories
- ✅ Product specifications
- ✅ Realistic pricing in South African Rand

Perfect for testing and creating test cases!

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
    --bg-secondary: #1a1a1a;
}
```

## Troubleshooting

### No products showing up?
- Make sure you're using the included `db.sqlite3` file from the repository
- If you deleted it, follow the "Alternative Setup" instructions above

### Can't login as admin?
- Username: `admin`
- Password: `admin123`
- If this doesn't work, you may have created a fresh database. Use the credentials you set during `createsuperuser`

### Server won't start?
- Make sure your virtual environment is activated
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Ensure you're in the correct directory (where `manage.py` is located)

## License

This project is for educational purposes.

## Repository

https://github.com/Del1rius/techstore

## Support

For issues or questions, please check the Django documentation at https://docs.djangoproject.com/
