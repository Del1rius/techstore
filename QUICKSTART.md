# Quick Start Guide

## Start the Server

```bash
# Activate virtual environment (if not already activated)
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# Start the development server
python manage.py runserver
```

## Access the Application

- **Main Website**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin

## Default Login Credentials

### Admin User
- **Username**: `admin`
- **Password**: `admin123`

## Quick Test Flow

1. **Visit the homepage** at http://127.0.0.1:8000
2. **Register a new user** or login with existing credentials
3. **Browse products** - Click "Products" or "Shop Now"
4. **Filter and search** - Use the filter section to find products
5. **View product details** - Click on any product
6. **Add to cart** - Must be logged in
7. **View cart** - Click the cart icon in navigation
8. **Update quantities** - Change quantities in cart
9. **Checkout** - Complete your order
10. **Admin panel** - Login at /admin to manage products

## Features to Test

### User Features
- ✅ User registration and login
- ✅ Browse 50+ tech products
- ✅ Search products by name/description
- ✅ Filter by category (10 categories)
- ✅ Sort by price, name, newest
- ✅ Add/remove items from cart
- ✅ Update cart quantities
- ✅ Checkout process
- ✅ Stock validation

### Admin Features (login at /admin)
- ✅ Manage categories
- ✅ Add/edit/delete products
- ✅ View all orders
- ✅ Manage users
- ✅ Update stock levels

## Product Categories

1. Laptops (7 products)
2. Desktops (6 products)
3. Monitors (7 products)
4. Keyboards (6 products)
5. Mice (6 products)
6. Headphones (7 products)
7. Webcams (5 products)
8. Speakers (5 products)
9. Graphics Cards (6 products)
10. Processors (6 products)

**Total: 61 products**

## Troubleshooting

### Port Already in Use
If port 8000 is busy, use a different port:
```bash
python manage.py runserver 8080
```

### Database Issues
Reset the database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py populate_db
```

### Static Files Warning
This is normal in development mode. Static files are served automatically.

## Next Steps

- Customize the theme colors in `templates/base.html`
- Add more products via admin panel
- Create additional user accounts
- Test the complete shopping flow
- Explore the admin panel features

Enjoy your TechStore! 🚀
