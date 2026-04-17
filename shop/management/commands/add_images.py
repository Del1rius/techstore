from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = 'Add image URLs to products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding images to products...')
        
        # Generic tech product images from Unsplash
        image_mappings = {
            # Laptops
            'MacBook Pro 16"': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&h=500&fit=crop',
            'Dell XPS 15': 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=500&h=500&fit=crop',
            'HP Spectre x360': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&h=500&fit=crop',
            'Lenovo ThinkPad X1': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500&h=500&fit=crop',
            'ASUS ROG Zephyrus': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=500&h=500&fit=crop',
            'Acer Swift 3': 'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=500&h=500&fit=crop',
            'Microsoft Surface Laptop': 'https://images.unsplash.com/photo-1587614382346-4ec70e388b28?w=500&h=500&fit=crop',
            
            # Desktops
            'iMac 24"': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500&h=500&fit=crop',
            'Dell Inspiron Desktop': 'https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=500&h=500&fit=crop',
            'HP Pavilion Gaming': 'https://images.unsplash.com/photo-1593640408182-31c70c8268f5?w=500&h=500&fit=crop',
            'Alienware Aurora': 'https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=500&h=500&fit=crop',
            'ASUS ROG Strix': 'https://images.unsplash.com/photo-1591238371159-c0e5e4f98e4e?w=500&h=500&fit=crop',
            'Lenovo IdeaCentre': 'https://images.unsplash.com/photo-1587202372583-49330a15584d?w=500&h=500&fit=crop',
            
            # Monitors
            'LG UltraGear 27"': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&h=500&fit=crop',
            'Samsung Odyssey G7': 'https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=500&h=500&fit=crop',
            'Dell UltraSharp 32"': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500&h=500&fit=crop',
            'ASUS ProArt Display': 'https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=500&h=500&fit=crop',
            'BenQ PD2700U': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&h=500&fit=crop',
            'Acer Predator X34': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500&h=500&fit=crop',
            'ViewSonic VP2468': 'https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=500&h=500&fit=crop',
            
            # Keyboards
            'Logitech MX Keys': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500&h=500&fit=crop',
            'Corsair K95 RGB': 'https://images.unsplash.com/photo-1595225476474-87563907a212?w=500&h=500&fit=crop',
            'Razer BlackWidow V3': 'https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=500&h=500&fit=crop',
            'Keychron K8': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500&h=500&fit=crop',
            'SteelSeries Apex Pro': 'https://images.unsplash.com/photo-1595225476474-87563907a212?w=500&h=500&fit=crop',
            'Das Keyboard 4': 'https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=500&h=500&fit=crop',
            
            # Mice
            'Logitech MX Master 3': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&h=500&fit=crop',
            'Razer DeathAdder V3': 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500&h=500&fit=crop',
            'Logitech G Pro X': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&h=500&fit=crop',
            'Corsair Dark Core RGB': 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500&h=500&fit=crop',
            'SteelSeries Rival 3': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&h=500&fit=crop',
            'Razer Basilisk V3': 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500&h=500&fit=crop',
            
            # Headphones
            'Sony WH-1000XM5': 'https://images.unsplash.com/photo-1545127398-14699f92334b?w=500&h=500&fit=crop',
            'Bose QuietComfort 45': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500&h=500&fit=crop',
            'SteelSeries Arctis 7': 'https://images.unsplash.com/photo-1599669454699-248893623440?w=500&h=500&fit=crop',
            'HyperX Cloud II': 'https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=500&h=500&fit=crop',
            'Razer BlackShark V2': 'https://images.unsplash.com/photo-1599669454699-248893623440?w=500&h=500&fit=crop',
            'Audio-Technica ATH-M50x': 'https://images.unsplash.com/photo-1545127398-14699f92334b?w=500&h=500&fit=crop',
            
            # Webcams
            'Logitech C920': 'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=500&h=500&fit=crop',
            'Razer Kiyo Pro': 'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=500&h=500&fit=crop',
            'Logitech Brio 4K': 'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=500&h=500&fit=crop',
            'Elgato Facecam': 'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=500&h=500&fit=crop',
            'Microsoft LifeCam HD': 'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=500&h=500&fit=crop',
            
            # Speakers
            'Logitech Z623': 'https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500&h=500&fit=crop',
            'Bose Companion 2': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500&h=500&fit=crop',
            'Audioengine A2+': 'https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500&h=500&fit=crop',
            'Creative Pebble V3': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500&h=500&fit=crop',
            'Razer Nommo Chroma': 'https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500&h=500&fit=crop',
            
            # Graphics Cards
            'NVIDIA RTX 4090': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500&h=500&fit=crop',
            'NVIDIA RTX 4080': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500&h=500&fit=crop',
            'NVIDIA RTX 4070 Ti': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500&h=500&fit=crop',
            'AMD Radeon RX 7900 XTX': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500&h=500&fit=crop',
            'NVIDIA RTX 4060 Ti': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500&h=500&fit=crop',
            'AMD Radeon RX 7800 XT': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500&h=500&fit=crop',
            
            # Processors
            'Intel Core i9-14900K': 'https://images.unsplash.com/photo-1555617981-dac3880eac6e?w=500&h=500&fit=crop',
            'AMD Ryzen 9 7950X': 'https://images.unsplash.com/photo-1555617981-dac3880eac6e?w=500&h=500&fit=crop',
            'Intel Core i7-14700K': 'https://images.unsplash.com/photo-1555617981-dac3880eac6e?w=500&h=500&fit=crop',
            'AMD Ryzen 7 7800X3D': 'https://images.unsplash.com/photo-1555617981-dac3880eac6e?w=500&h=500&fit=crop',
            'Intel Core i5-14600K': 'https://images.unsplash.com/photo-1555617981-dac3880eac6e?w=500&h=500&fit=crop',
            'AMD Ryzen 5 7600X': 'https://images.unsplash.com/photo-1555617981-dac3880eac6e?w=500&h=500&fit=crop',
        }
        
        updated_count = 0
        for product_name, image_url in image_mappings.items():
            try:
                product = Product.objects.get(name=product_name)
                product.image_url = image_url
                product.save()
                updated_count += 1
                self.stdout.write(f'Updated image for: {product_name}')
            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Product not found: {product_name}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} product images!'))
