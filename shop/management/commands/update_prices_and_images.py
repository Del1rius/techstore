from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = 'Update product prices to reflect real market prices and fix motherboard images'

    def handle(self, *args, **kwargs):
        self.stdout.write('Updating prices and images...')
        
        # Motherboard image (generic motherboard from Unsplash)
        motherboard_image = 'https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=500&h=500&fit=crop'
        
        # RAM image
        ram_image = 'https://images.unsplash.com/photo-1541029071515-84cc54f84dc5?w=500&h=500&fit=crop'
        
        # Update prices and images (prices in South African Rand)
        updates = {
            # CPUs - Updated to realistic SA prices
            'AMD Ryzen 9 7950X3D': {'price': 10499.00, 'image': None},
            'AMD Ryzen 9 9950X': {'price': 11999.00, 'image': None},
            'AMD Ryzen 9 7950X': {'price': 9999.00, 'image': None},
            'AMD Ryzen 7 9700X': {'price': 6299.00, 'image': None},
            'AMD Ryzen 7 7800X3D': {'price': 7499.00, 'image': None},
            'AMD Ryzen 5 9600X': {'price': 4799.00, 'image': None},
            'AMD Ryzen 5 7600X': {'price': 3999.00, 'image': None},
            'AMD Ryzen 5 7600': {'price': 3499.00, 'image': None},
            'Intel Core i9-14900KS': {'price': 13999.00, 'image': None},
            'Intel Core i9-14900K': {'price': 10999.00, 'image': None},
            'Intel Core i7-14700K': {'price': 7999.00, 'image': None},
            'Intel Core i7-13700K': {'price': 6999.00, 'image': None},
            'Intel Core i5-14600K': {'price': 5499.00, 'image': None},
            'Intel Core i5-13600K': {'price': 4999.00, 'image': None},
            
            # GPUs - Updated to realistic SA prices
            'NVIDIA RTX 4090 Ti': {'price': 39999.00, 'image': None},
            'NVIDIA RTX 4090': {'price': 34999.00, 'image': None},
            'NVIDIA RTX 4080': {'price': 21999.00, 'image': None},
            'NVIDIA RTX 4070 Ti': {'price': 14999.00, 'image': None},
            'NVIDIA RTX 4070 Super': {'price': 11999.00, 'image': None},
            'NVIDIA RTX 4060 Ti': {'price': 8499.00, 'image': None},
            'NVIDIA RTX 4060': {'price': 6499.00, 'image': None},
            'NVIDIA RTX 3060 Ti': {'price': 7499.00, 'image': None},
            'AMD Radeon RX 7900 XTX': {'price': 17999.00, 'image': None},
            'AMD Radeon RX 7900 XT': {'price': 14999.00, 'image': None},
            'AMD Radeon RX 7800 XT': {'price': 9999.00, 'image': None},
            'AMD Radeon RX 7700 XT': {'price': 8499.00, 'image': None},
            'AMD Radeon RX 7600': {'price': 5299.00, 'image': None},
            'AMD Radeon RX 6700 XT': {'price': 6499.00, 'image': None},
            
            # RAM - Updated to realistic SA prices
            'Corsair Vengeance DDR5 32GB (2x16GB) 6000MHz': {'price': 2299.00, 'image': ram_image},
            'G.Skill Trident Z5 RGB 32GB (2x16GB) 6400MHz': {'price': 2799.00, 'image': ram_image},
            'Kingston Fury Beast DDR5 16GB (2x8GB) 5200MHz': {'price': 1199.00, 'image': ram_image},
            'Corsair Vengeance DDR5 64GB (2x32GB) 5600MHz': {'price': 4299.00, 'image': ram_image},
            'TeamGroup T-Force Delta RGB DDR5 32GB (2x16GB) 6000MHz': {'price': 2199.00, 'image': ram_image},
            'Corsair Vengeance LPX DDR4 32GB (2x16GB) 3600MHz': {'price': 1599.00, 'image': ram_image},
            'G.Skill Ripjaws V DDR4 16GB (2x8GB) 3200MHz': {'price': 799.00, 'image': ram_image},
            'Kingston Fury Beast RGB DDR4 32GB (2x16GB) 3600MHz': {'price': 1799.00, 'image': ram_image},
            
            # Motherboards - Updated to realistic SA prices and fix images
            'ASUS ROG Maximus Z790 Hero': {'price': 8999.00, 'image': motherboard_image},
            'MSI MAG Z790 Tomahawk WiFi': {'price': 5999.00, 'image': motherboard_image},
            'Gigabyte Z790 AORUS Elite AX': {'price': 4999.00, 'image': motherboard_image},
            'ASRock Z790 Pro RS': {'price': 3499.00, 'image': motherboard_image},
            'ASUS Prime B760-PLUS': {'price': 2799.00, 'image': motherboard_image},
            'ASUS ROG Crosshair X670E Hero': {'price': 9999.00, 'image': motherboard_image},
            'MSI MAG X670E Tomahawk WiFi': {'price': 6499.00, 'image': motherboard_image},
            'Gigabyte B650 AORUS Elite AX': {'price': 3999.00, 'image': motherboard_image},
            'ASRock B650M Pro RS': {'price': 2499.00, 'image': motherboard_image},
            'ASUS TUF Gaming B650-PLUS WiFi': {'price': 3499.00, 'image': motherboard_image},
            
            # Laptops - Updated to realistic SA prices
            'MacBook Pro 16"': {'price': 54999.00, 'image': None},
            'Dell XPS 15': {'price': 32999.00, 'image': None},
            'HP Spectre x360': {'price': 28999.00, 'image': None},
            'Lenovo ThinkPad X1': {'price': 29999.00, 'image': None},
            'ASUS ROG Zephyrus': {'price': 39999.00, 'image': None},
            'Acer Swift 3': {'price': 14999.00, 'image': None},
            'Microsoft Surface Laptop': {'price': 24999.00, 'image': None},
            
            # Desktops - Updated to realistic SA prices
            'iMac 24"': {'price': 34999.00, 'image': None},
            'Dell Inspiron Desktop': {'price': 12999.00, 'image': None},
            'HP Pavilion Gaming': {'price': 16999.00, 'image': None},
            'Alienware Aurora': {'price': 44999.00, 'image': None},
            'ASUS ROG Strix': {'price': 49999.00, 'image': None},
            'Lenovo IdeaCentre': {'price': 11999.00, 'image': None},
            
            # Monitors - Updated to realistic SA prices
            'LG UltraGear 27"': {'price': 6999.00, 'image': None},
            'Samsung Odyssey G7': {'price': 9999.00, 'image': None},
            'Dell UltraSharp 32"': {'price': 14999.00, 'image': None},
            'ASUS ProArt Display': {'price': 12999.00, 'image': None},
            'BenQ PD2700U': {'price': 11999.00, 'image': None},
            'Acer Predator X34': {'price': 15999.00, 'image': None},
            'ViewSonic VP2468': {'price': 5999.00, 'image': None},
            
            # Keyboards - Updated to realistic SA prices
            'Logitech MX Keys': {'price': 1999.00, 'image': None},
            'Corsair K95 RGB': {'price': 3499.00, 'image': None},
            'Razer BlackWidow V3': {'price': 2499.00, 'image': None},
            'Keychron K8': {'price': 1799.00, 'image': None},
            'SteelSeries Apex Pro': {'price': 3999.00, 'image': None},
            'Das Keyboard 4': {'price': 2799.00, 'image': None},
            
            # Mice - Updated to realistic SA prices
            'Logitech MX Master 3': {'price': 1499.00, 'image': None},
            'Razer DeathAdder V3': {'price': 1299.00, 'image': None},
            'Logitech G Pro X': {'price': 1799.00, 'image': None},
            'Corsair Dark Core RGB': {'price': 1599.00, 'image': None},
            'SteelSeries Rival 3': {'price': 699.00, 'image': None},
            'Razer Basilisk V3': {'price': 1399.00, 'image': None},
            
            # Headphones - Updated to realistic SA prices
            'Sony WH-1000XM5': {'price': 6999.00, 'image': None},
            'Bose QuietComfort 45': {'price': 6499.00, 'image': None},
            'SteelSeries Arctis 7': {'price': 2999.00, 'image': None},
            'HyperX Cloud II': {'price': 1799.00, 'image': None},
            'Razer BlackShark V2': {'price': 1999.00, 'image': None},
            'Audio-Technica ATH-M50x': {'price': 2499.00, 'image': None},
            
            # Webcams - Updated to realistic SA prices
            'Logitech C920': {'price': 1299.00, 'image': None},
            'Razer Kiyo Pro': {'price': 2499.00, 'image': None},
            'Logitech Brio 4K': {'price': 3499.00, 'image': None},
            'Elgato Facecam': {'price': 2799.00, 'image': None},
            'Microsoft LifeCam HD': {'price': 899.00, 'image': None},
            
            # Speakers - Updated to realistic SA prices
            'Logitech Z623': {'price': 2499.00, 'image': None},
            'Bose Companion 2': {'price': 3999.00, 'image': None},
            'Audioengine A2+': {'price': 5999.00, 'image': None},
            'Creative Pebble V3': {'price': 899.00, 'image': None},
            'Razer Nommo Chroma': {'price': 2999.00, 'image': None},
        }
        
        updated_count = 0
        for product_name, data in updates.items():
            try:
                product = Product.objects.get(name=product_name)
                product.price = data['price']
                if data['image']:
                    product.image_url = data['image']
                product.save()
                updated_count += 1
                self.stdout.write(f'Updated: {product_name} - R{data["price"]}')
            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Product not found: {product_name}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} products!'))
