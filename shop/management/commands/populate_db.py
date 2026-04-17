from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shop.models import Category, Product
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Populate database with categories and products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating categories...')
        
        categories_data = [
            'Laptops',
            'Desktops',
            'Monitors',
            'Keyboards',
            'Mice',
            'Headphones',
            'Webcams',
            'Speakers',
            'Graphics Cards',
            'Processors',
        ]
        
        categories = {}
        for cat_name in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_name,
                slug=slugify(cat_name)
            )
            categories[cat_name] = cat
            if created:
                self.stdout.write(f'Created category: {cat_name}')
        
        self.stdout.write('Creating products...')
        
        products_data = [
            # Laptops
            ('MacBook Pro 16"', 'Laptops', 'Powerful laptop with M3 chip, 16GB RAM, 512GB SSD', 2499.99, 15),
            ('Dell XPS 15', 'Laptops', 'Premium laptop with Intel i7, 16GB RAM, 1TB SSD', 1899.99, 20),
            ('HP Spectre x360', 'Laptops', 'Convertible laptop with touchscreen, Intel i7, 16GB RAM', 1599.99, 12),
            ('Lenovo ThinkPad X1', 'Laptops', 'Business laptop with Intel i7, 16GB RAM, 512GB SSD', 1799.99, 18),
            ('ASUS ROG Zephyrus', 'Laptops', 'Gaming laptop with RTX 4070, AMD Ryzen 9, 32GB RAM', 2299.99, 10),
            ('Acer Swift 3', 'Laptops', 'Lightweight laptop with AMD Ryzen 5, 8GB RAM, 512GB SSD', 799.99, 25),
            ('Microsoft Surface Laptop', 'Laptops', 'Sleek laptop with Intel i5, 8GB RAM, 256GB SSD', 1299.99, 14),
            
            # Desktops
            ('iMac 24"', 'Desktops', 'All-in-one desktop with M3 chip, 8GB RAM, 256GB SSD', 1499.99, 10),
            ('Dell Inspiron Desktop', 'Desktops', 'Tower desktop with Intel i5, 16GB RAM, 1TB HDD', 899.99, 15),
            ('HP Pavilion Gaming', 'Desktops', 'Gaming desktop with RTX 3060, Intel i7, 16GB RAM', 1399.99, 12),
            ('Alienware Aurora', 'Desktops', 'High-end gaming desktop with RTX 4080, Intel i9, 32GB RAM', 3299.99, 8),
            ('ASUS ROG Strix', 'Desktops', 'Gaming desktop with RTX 4070, AMD Ryzen 7, 16GB RAM', 1899.99, 10),
            ('Lenovo IdeaCentre', 'Desktops', 'Compact desktop with Intel i3, 8GB RAM, 512GB SSD', 649.99, 20),
            
            # Monitors
            ('LG UltraGear 27"', 'Monitors', '4K gaming monitor, 144Hz, 1ms response time', 599.99, 18),
            ('Samsung Odyssey G7', 'Monitors', 'Curved gaming monitor, 240Hz, QLED, 27"', 699.99, 15),
            ('Dell UltraSharp 32"', 'Monitors', '4K professional monitor, IPS, USB-C hub', 899.99, 12),
            ('ASUS ProArt Display', 'Monitors', '4K color-accurate monitor for creators, 27"', 799.99, 10),
            ('BenQ PD2700U', 'Monitors', '4K designer monitor with CAD/CAM mode, 27"', 549.99, 14),
            ('Acer Predator X34', 'Monitors', 'Ultrawide curved gaming monitor, 144Hz, 34"', 999.99, 8),
            ('ViewSonic VP2468', 'Monitors', 'Professional monitor with color calibration, 24"', 399.99, 20),
            
            # Keyboards
            ('Logitech MX Keys', 'Keyboards', 'Wireless illuminated keyboard for productivity', 99.99, 30),
            ('Corsair K95 RGB', 'Keyboards', 'Mechanical gaming keyboard with Cherry MX switches', 199.99, 25),
            ('Razer BlackWidow V3', 'Keyboards', 'Mechanical gaming keyboard with green switches', 139.99, 28),
            ('Keychron K8', 'Keyboards', 'Wireless mechanical keyboard, hot-swappable', 89.99, 35),
            ('SteelSeries Apex Pro', 'Keyboards', 'Adjustable mechanical gaming keyboard', 179.99, 20),
            ('Das Keyboard 4', 'Keyboards', 'Professional mechanical keyboard with media controls', 169.99, 15),
            
            # Mice
            ('Logitech MX Master 3', 'Mice', 'Wireless productivity mouse with ergonomic design', 99.99, 40),
            ('Razer DeathAdder V3', 'Mice', 'Ergonomic gaming mouse with 30K DPI sensor', 69.99, 35),
            ('Logitech G Pro X', 'Mice', 'Lightweight wireless gaming mouse, 25K sensor', 149.99, 30),
            ('Corsair Dark Core RGB', 'Mice', 'Wireless gaming mouse with Qi charging', 89.99, 25),
            ('SteelSeries Rival 3', 'Mice', 'Budget gaming mouse with TrueMove Core sensor', 29.99, 50),
            ('Razer Basilisk V3', 'Mice', 'Customizable gaming mouse with 11 buttons', 59.99, 32),
            
            # Headphones
            ('Sony WH-1000XM5', 'Headphones', 'Premium noise-cancelling wireless headphones', 399.99, 20),
            ('Bose QuietComfort 45', 'Headphones', 'Wireless noise-cancelling headphones', 329.99, 22),
            ('SteelSeries Arctis 7', 'Headphones', 'Wireless gaming headset with DTS Headphone:X', 149.99, 28),
            ('HyperX Cloud II', 'Headphones', 'Gaming headset with 7.1 surround sound', 99.99, 35),
            ('Razer BlackShark V2', 'Headphones', 'Esports gaming headset with THX Spatial Audio', 99.99, 30),
            ('Audio-Technica ATH-M50x', 'Headphones', 'Professional studio monitor headphones', 149.99, 25),
            ('Logitech G Pro X', 'Headphones', 'Gaming headset with Blue VO!CE technology', 129.99, 24),
            
            # Webcams
            ('Logitech C920', 'Webcams', '1080p HD webcam with stereo audio', 79.99, 40),
            ('Razer Kiyo Pro', 'Webcams', '1080p webcam with HDR and wide-angle lens', 199.99, 18),
            ('Logitech Brio 4K', 'Webcams', '4K Ultra HD webcam with HDR', 199.99, 20),
            ('Elgato Facecam', 'Webcams', '1080p60 webcam for streaming', 169.99, 15),
            ('Microsoft LifeCam HD', 'Webcams', '720p HD webcam for video calls', 39.99, 45),
            
            # Speakers
            ('Logitech Z623', 'Speakers', '2.1 speaker system with 200W RMS power', 129.99, 25),
            ('Bose Companion 2', 'Speakers', 'Desktop speakers with clear sound', 99.99, 30),
            ('Audioengine A2+', 'Speakers', 'Premium desktop speakers with Bluetooth', 269.99, 15),
            ('Creative Pebble V3', 'Speakers', 'Compact USB-C desktop speakers with RGB', 34.99, 50),
            ('Razer Nommo Chroma', 'Speakers', 'Gaming speakers with RGB lighting', 149.99, 20),
            
            # Graphics Cards
            ('NVIDIA RTX 4090', 'Graphics Cards', 'Flagship GPU with 24GB GDDR6X', 1599.99, 5),
            ('NVIDIA RTX 4080', 'Graphics Cards', 'High-end GPU with 16GB GDDR6X', 1199.99, 8),
            ('NVIDIA RTX 4070 Ti', 'Graphics Cards', 'Performance GPU with 12GB GDDR6X', 799.99, 12),
            ('AMD Radeon RX 7900 XTX', 'Graphics Cards', 'High-end AMD GPU with 24GB GDDR6', 999.99, 10),
            ('NVIDIA RTX 4060 Ti', 'Graphics Cards', 'Mid-range GPU with 8GB GDDR6', 399.99, 15),
            ('AMD Radeon RX 7800 XT', 'Graphics Cards', 'Performance AMD GPU with 16GB GDDR6', 499.99, 14),
            
            # Processors
            ('Intel Core i9-14900K', 'Processors', '24-core processor, 6.0GHz max turbo', 589.99, 12),
            ('AMD Ryzen 9 7950X', 'Processors', '16-core processor, 5.7GHz max boost', 549.99, 15),
            ('Intel Core i7-14700K', 'Processors', '20-core processor, 5.6GHz max turbo', 409.99, 18),
            ('AMD Ryzen 7 7800X3D', 'Processors', '8-core gaming processor with 3D V-Cache', 449.99, 14),
            ('Intel Core i5-14600K', 'Processors', '14-core processor, 5.3GHz max turbo', 319.99, 20),
            ('AMD Ryzen 5 7600X', 'Processors', '6-core processor, 5.3GHz max boost', 229.99, 25),
        ]
        
        for name, cat_name, desc, price, stock in products_data:
            product, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    'slug': slugify(name),
                    'category': categories[cat_name],
                    'description': desc,
                    'price': price,
                    'stock': stock,
                }
            )
            if created:
                self.stdout.write(f'Created product: {name}')
        
        # Create admin user
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@techstore.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Created admin user (username: admin, password: admin123)'))
        
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
