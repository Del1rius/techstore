# Getting Started with TechStore

## 🎯 Your E-commerce Platform is Ready!

The Django development server is currently running at: **http://127.0.0.1:8000**

## 🚀 Quick Access

### Main Website
Open your browser and go to: **http://127.0.0.1:8000**

### Admin Panel
Go to: **http://127.0.0.1:8000/admin**
- Username: `admin`
- Password: `admin123`

## 👤 Test the Application

### Option 1: Use Admin Account
- Username: `admin`
- Password: `admin123`

### Option 2: Register a New Account
1. Click "Register" in the navigation
2. Create your account
3. Login and start shopping

### Option 3: Create Test Users
```bash
python manage.py create_test_users
```
This creates:
- john / test123
- jane / test123
- bob / test123

## 🛍️ Shopping Flow

### 1. Browse Products
- Visit the homepage
- Click "Shop Now" or "Products" in navigation
- View 61 tech products across 10 categories

### 2. Search & Filter
- Use the search bar to find products
- Filter by category (Laptops, Monitors, etc.)
- Sort by price, name, or newest

### 3. View Product Details
- Click on any product card
- See full description, price, and stock
- Note: Must login to add to cart

### 4. Add to Cart
- Login first (required)
- Click "Add to Cart" on product page
- See cart count update in navbar

### 5. Manage Cart
- Click cart icon in navigation
- Update quantities
- Remove items
- See total price

### 6. Checkout
- Click "Checkout" button
- Order is created
- Stock is automatically updated
- Redirected to homepage

## 🎨 Features to Explore

### For Shoppers
✅ Browse 61 products
✅ Search by name/description
✅ Filter by 10 categories
✅ Sort by price/name/date
✅ View detailed product info
✅ Add/remove cart items
✅ Update quantities
✅ Complete checkout

### For Admins
✅ Full product management
✅ Category management
✅ Order tracking
✅ User management
✅ Stock control
✅ Price updates

## 📱 Navigation Guide

### Main Navigation Bar
- **Home**: Featured products and info
- **Products**: Full product catalog with filters
- **Cart**: Your shopping cart (when logged in)
- **Login/Register**: User authentication
- **Logout**: Sign out (when logged in)

### Product List Page
- **Search Box**: Find products by name/description
- **Category Filter**: Select specific category
- **Sort Dropdown**: Order by price, name, or date
- **Filter Button**: Apply your selections

### Product Card
- **Product Image**: Icon representation
- **Product Name**: Full product name
- **Description**: Brief overview
- **Category Badge**: Product category
- **Stock Badge**: Available quantity
- **Price**: Current price
- **View Button**: See full details

## 🎨 Theme & Design

### Color Scheme
- **Black Background**: Modern, sleek look
- **Purple Accents**: Primary brand color
- **Gradient Effects**: Smooth transitions
- **Card Hover**: Interactive feedback

### Responsive Design
- Works on desktop, tablet, and mobile
- Bootstrap 5 framework
- Modern, clean interface

## 🔧 Admin Panel Guide

### Access Admin
1. Go to http://127.0.0.1:8000/admin
2. Login with admin/admin123
3. See Django admin dashboard

### Manage Products
1. Click "Products" in admin
2. View all 61 products
3. Click any product to edit
4. Update name, price, stock, description
5. Save changes

### Add New Product
1. Click "Add Product"
2. Fill in required fields:
   - Name
   - Slug (auto-generated from name)
   - Category
   - Description
   - Price
   - Stock
3. Click "Save"

### Manage Categories
1. Click "Categories"
2. Add/edit/delete categories
3. Each category has name and slug

### View Orders
1. Click "Orders"
2. See all customer orders
3. View order details and items
4. Check total amounts

## 📊 Product Inventory

### Categories & Count
1. Laptops (7)
2. Desktops (6)
3. Monitors (7)
4. Keyboards (6)
5. Mice (6)
6. Headphones (7)
7. Webcams (5)
8. Speakers (5)
9. Graphics Cards (6)
10. Processors (6)

**Total: 61 Products**

### Price Range
- Budget: $29.99 - $99.99
- Mid-range: $100 - $499.99
- Premium: $500 - $999.99
- High-end: $1000+

### Stock Levels
- All products have initial stock
- Stock decreases on checkout
- Admin can update stock levels

## 🎯 Testing Scenarios

### Scenario 1: Guest Browsing
1. Visit homepage without login
2. Browse products
3. Try to add to cart → Prompted to login
4. Register new account
5. Now can add to cart

### Scenario 2: Shopping Flow
1. Login as user
2. Search for "laptop"
3. Filter by Laptops category
4. Sort by price (low to high)
5. Click on a product
6. Add to cart
7. Continue shopping
8. Add more items
9. View cart
10. Update quantities
11. Checkout

### Scenario 3: Admin Management
1. Login to admin panel
2. Add a new product
3. Update stock for existing product
4. View recent orders
5. Check customer list

## 🛠️ Troubleshooting

### Can't Access Website?
- Check server is running
- Look for "Starting development server at http://127.0.0.1:8000/"
- Try http://localhost:8000 instead

### Can't Login?
- Check username/password
- Admin: admin / admin123
- Or register a new account

### Cart Not Working?
- Make sure you're logged in
- Check product has stock available

### Admin Panel Not Loading?
- Verify URL: http://127.0.0.1:8000/admin
- Use admin credentials
- Check server is running

## 📝 Useful Commands

### Server Management
```bash
# Start server
python manage.py runserver

# Start on different port
python manage.py runserver 8080

# Stop server
Press CTRL+C
```

### Database Management
```bash
# Reset database
rm db.sqlite3
python manage.py migrate
python manage.py populate_db

# Create new admin
python manage.py createsuperuser

# Create test users
python manage.py create_test_users
```

### Development
```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Open Django shell
python manage.py shell
```

## 🎓 What You Have

### Complete E-commerce System
✅ User authentication
✅ Product catalog
✅ Shopping cart
✅ Checkout process
✅ Admin panel
✅ Stock management
✅ Order tracking
✅ Modern UI/UX

### Professional Features
✅ Search functionality
✅ Category filtering
✅ Product sorting
✅ Responsive design
✅ Form validation
✅ Security features
✅ Database relationships
✅ Session management

## 🌟 Next Actions

1. **Explore the site** - Browse products, test features
2. **Try admin panel** - Manage products and orders
3. **Test shopping flow** - Complete a full purchase
4. **Customize** - Modify colors, add products
5. **Learn** - Study the code structure

## 📚 Documentation Files

- **README.md**: Complete project documentation
- **QUICKSTART.md**: Quick start guide
- **PROJECT_SUMMARY.md**: Detailed project overview
- **GETTING_STARTED.md**: This file

## 🎉 You're All Set!

Your TechStore e-commerce platform is fully functional and ready to use!

**Start exploring at: http://127.0.0.1:8000**

Happy shopping! 🛒
