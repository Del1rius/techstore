from django.core.management.base import BaseCommand
from shop.models import Product, Category
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Add more CPUs, GPUs, RAM, and Motherboards'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding more products...')
        
        # Get or create categories
        cpu_category, _ = Category.objects.get_or_create(
            slug='processors',
            defaults={'name': 'Processors'}
        )
        gpu_category, _ = Category.objects.get_or_create(
            slug='graphics-cards',
            defaults={'name': 'Graphics Cards'}
        )
        
        # Create RAM category
        ram_category, _ = Category.objects.get_or_create(
            slug='ram',
            defaults={'name': 'RAM'}
        )
        
        # Create Motherboards category
        mobo_category, _ = Category.objects.get_or_create(
            slug='motherboards',
            defaults={'name': 'Motherboards'}
        )
        
        products = [
            # Additional AMD CPUs
            {
                'name': 'AMD Ryzen 9 7950X3D',
                'category': cpu_category,
                'description': '16-core processor with 3D V-Cache technology for ultimate gaming performance',
                'price': 10999.99,
                'stock': 8,
                'specifications': """16 cores, 32 threads
Up to 5.7 GHz boost clock
144MB total cache (with 3D V-Cache)
120W TDP
AM5 socket
DDR5-5200 support
PCIe 5.0 support
Integrated RDNA 2 graphics
3D V-Cache technology for gaming"""
            },
            {
                'name': 'AMD Ryzen 9 9950X',
                'category': cpu_category,
                'description': 'Latest Zen 5 architecture, 16-core powerhouse for content creation',
                'price': 11499.99,
                'stock': 6,
                'specifications': """16 cores, 32 threads
Up to 5.7 GHz boost clock
80MB total cache
170W TDP
AM5 socket
DDR5-5600 support
PCIe 5.0 support
Zen 5 architecture
Integrated RDNA 2 graphics"""
            },
            {
                'name': 'AMD Ryzen 7 9700X',
                'category': cpu_category,
                'description': '8-core Zen 5 processor with excellent efficiency',
                'price': 6499.99,
                'stock': 12,
                'specifications': """8 cores, 16 threads
Up to 5.5 GHz boost clock
40MB total cache
65W TDP
AM5 socket
DDR5-5600 support
PCIe 5.0 support
Zen 5 architecture
Integrated RDNA 2 graphics"""
            },
            {
                'name': 'AMD Ryzen 5 9600X',
                'category': cpu_category,
                'description': '6-core Zen 5 processor perfect for gaming and productivity',
                'price': 4999.99,
                'stock': 15,
                'specifications': """6 cores, 12 threads
Up to 5.4 GHz boost clock
38MB total cache
65W TDP
AM5 socket
DDR5-5600 support
PCIe 5.0 support
Zen 5 architecture
Integrated RDNA 2 graphics"""
            },
            {
                'name': 'AMD Ryzen 5 7600',
                'category': cpu_category,
                'description': '6-core processor with great value for gaming builds',
                'price': 3999.99,
                'stock': 20,
                'specifications': """6 cores, 12 threads
Up to 5.1 GHz boost clock
38MB total cache
65W TDP
AM5 socket
DDR5-5200 support
PCIe 5.0 support
Integrated RDNA 2 graphics"""
            },
            
            # Additional Intel CPUs
            {
                'name': 'Intel Core i9-14900KS',
                'category': cpu_category,
                'description': 'Special edition with 6.2 GHz boost for extreme performance',
                'price': 12999.99,
                'stock': 5,
                'specifications': """24 cores (8P + 16E)
32 threads
Up to 6.2 GHz max turbo
36MB Intel Smart Cache
150W base power
LGA 1700 socket
DDR5-5600 support
PCIe 5.0 and 4.0 support
Intel UHD Graphics 770"""
            },
            {
                'name': 'Intel Core i7-13700K',
                'category': cpu_category,
                'description': '13th Gen processor with excellent multi-threaded performance',
                'price': 7499.99,
                'stock': 10,
                'specifications': """16 cores (8P + 8E)
24 threads
Up to 5.4 GHz max turbo
30MB Intel Smart Cache
125W base power
LGA 1700 socket
DDR5-5600 support
PCIe 5.0 and 4.0 support
Intel UHD Graphics 770"""
            },
            {
                'name': 'Intel Core i5-13600K',
                'category': cpu_category,
                'description': '13th Gen mid-range champion for gaming',
                'price': 5499.99,
                'stock': 18,
                'specifications': """14 cores (6P + 8E)
20 threads
Up to 5.1 GHz max turbo
24MB Intel Smart Cache
125W base power
LGA 1700 socket
DDR5-5600 support
PCIe 5.0 and 4.0 support
Intel UHD Graphics 770"""
            },
            
            # Additional NVIDIA GPUs
            {
                'name': 'NVIDIA RTX 4090 Ti',
                'category': gpu_category,
                'description': 'Ultimate flagship GPU for 8K gaming and professional work',
                'price': 34999.99,
                'stock': 3,
                'specifications': """24GB GDDR6X memory
18432 CUDA cores
2.6 GHz boost clock
Ada Lovelace architecture
Ray tracing cores (3rd gen)
Tensor cores (4th gen)
DLSS 3 support
PCIe 4.0 interface
600W TDP"""
            },
            {
                'name': 'NVIDIA RTX 4070 Super',
                'category': gpu_category,
                'description': 'Enhanced 4070 with better performance for 1440p gaming',
                'price': 11999.99,
                'stock': 12,
                'specifications': """12GB GDDR6X memory
7168 CUDA cores
2.48 GHz boost clock
Ada Lovelace architecture
Ray tracing cores (3rd gen)
Tensor cores (4th gen)
DLSS 3 support
PCIe 4.0 interface
220W TDP"""
            },
            {
                'name': 'NVIDIA RTX 4060',
                'category': gpu_category,
                'description': 'Excellent 1080p gaming GPU with ray tracing',
                'price': 6999.99,
                'stock': 25,
                'specifications': """8GB GDDR6 memory
3072 CUDA cores
2.46 GHz boost clock
Ada Lovelace architecture
Ray tracing cores (3rd gen)
Tensor cores (4th gen)
DLSS 3 support
PCIe 4.0 interface
115W TDP"""
            },
            {
                'name': 'NVIDIA RTX 3060 Ti',
                'category': gpu_category,
                'description': 'Great value 1440p gaming card',
                'price': 7999.99,
                'stock': 15,
                'specifications': """8GB GDDR6 memory
4864 CUDA cores
1.67 GHz boost clock
Ampere architecture
Ray tracing cores (2nd gen)
Tensor cores (3rd gen)
DLSS 2 support
PCIe 4.0 interface
200W TDP"""
            },
            
            # Additional AMD GPUs
            {
                'name': 'AMD Radeon RX 7900 XT',
                'category': gpu_category,
                'description': '20GB VRAM powerhouse for 4K gaming',
                'price': 14999.99,
                'stock': 8,
                'specifications': """20GB GDDR6 memory
5376 stream processors
2.4 GHz boost clock
RDNA 3 architecture
84 Ray Accelerators
84 AI Accelerators
DisplayPort 2.1 support
PCIe 4.0 interface
315W TDP"""
            },
            {
                'name': 'AMD Radeon RX 7700 XT',
                'category': gpu_category,
                'description': 'Excellent 1440p gaming with 12GB VRAM',
                'price': 8999.99,
                'stock': 14,
                'specifications': """12GB GDDR6 memory
3456 stream processors
2.54 GHz boost clock
RDNA 3 architecture
54 Ray Accelerators
54 AI Accelerators
DisplayPort 2.1 support
PCIe 4.0 interface
245W TDP"""
            },
            {
                'name': 'AMD Radeon RX 7600',
                'category': gpu_category,
                'description': 'Budget-friendly 1080p gaming champion',
                'price': 5499.99,
                'stock': 20,
                'specifications': """8GB GDDR6 memory
2048 stream processors
2.66 GHz boost clock
RDNA 3 architecture
32 Ray Accelerators
32 AI Accelerators
DisplayPort 2.1 support
PCIe 4.0 interface
165W TDP"""
            },
            {
                'name': 'AMD Radeon RX 6700 XT',
                'category': gpu_category,
                'description': 'Previous gen value with 12GB VRAM',
                'price': 6999.99,
                'stock': 10,
                'specifications': """12GB GDDR6 memory
2560 stream processors
2.58 GHz boost clock
RDNA 2 architecture
40 Ray Accelerators
Infinity Cache
DisplayPort 1.4 support
PCIe 4.0 interface
230W TDP"""
            },
            
            # DDR5 RAM
            {
                'name': 'Corsair Vengeance DDR5 32GB (2x16GB) 6000MHz',
                'category': ram_category,
                'description': 'High-performance DDR5 memory for gaming and content creation',
                'price': 2499.99,
                'stock': 30,
                'specifications': """32GB total capacity (2x16GB)
DDR5-6000 speed
CL30 latency
1.35V voltage
Intel XMP 3.0 support
AMD EXPO support
Heat spreader design
Lifetime warranty"""
            },
            {
                'name': 'G.Skill Trident Z5 RGB 32GB (2x16GB) 6400MHz',
                'category': ram_category,
                'description': 'Premium RGB DDR5 with extreme speeds',
                'price': 2999.99,
                'stock': 20,
                'specifications': """32GB total capacity (2x16GB)
DDR5-6400 speed
CL32 latency
1.40V voltage
Intel XMP 3.0 support
RGB lighting
Aluminum heat spreader
Lifetime warranty"""
            },
            {
                'name': 'Kingston Fury Beast DDR5 16GB (2x8GB) 5200MHz',
                'category': ram_category,
                'description': 'Reliable DDR5 memory for mainstream builds',
                'price': 1299.99,
                'stock': 40,
                'specifications': """16GB total capacity (2x8GB)
DDR5-5200 speed
CL40 latency
1.25V voltage
Intel XMP 3.0 support
Low-profile heat spreader
Plug N Play
Lifetime warranty"""
            },
            {
                'name': 'Corsair Vengeance DDR5 64GB (2x32GB) 5600MHz',
                'category': ram_category,
                'description': 'High-capacity DDR5 for workstations and heavy multitasking',
                'price': 4499.99,
                'stock': 15,
                'specifications': """64GB total capacity (2x32GB)
DDR5-5600 speed
CL40 latency
1.25V voltage
Intel XMP 3.0 support
AMD EXPO support
Heat spreader design
Lifetime warranty"""
            },
            {
                'name': 'TeamGroup T-Force Delta RGB DDR5 32GB (2x16GB) 6000MHz',
                'category': ram_category,
                'description': 'Stylish RGB DDR5 with great performance',
                'price': 2299.99,
                'stock': 25,
                'specifications': """32GB total capacity (2x16GB)
DDR5-6000 speed
CL30 latency
1.35V voltage
Intel XMP 3.0 support
120° ultra-wide lighting
Aluminum heat spreader
Lifetime warranty"""
            },
            
            # DDR4 RAM
            {
                'name': 'Corsair Vengeance LPX DDR4 32GB (2x16GB) 3600MHz',
                'category': ram_category,
                'description': 'Popular DDR4 memory for Intel and AMD systems',
                'price': 1799.99,
                'stock': 35,
                'specifications': """32GB total capacity (2x16GB)
DDR4-3600 speed
CL18 latency
1.35V voltage
Intel XMP 2.0 support
Low-profile design
Heat spreader
Lifetime warranty"""
            },
            {
                'name': 'G.Skill Ripjaws V DDR4 16GB (2x8GB) 3200MHz',
                'category': ram_category,
                'description': 'Reliable DDR4 for budget gaming builds',
                'price': 899.99,
                'stock': 50,
                'specifications': """16GB total capacity (2x8GB)
DDR4-3200 speed
CL16 latency
1.35V voltage
Intel XMP 2.0 support
Classic heat spreader design
Tested compatibility
Lifetime warranty"""
            },
            {
                'name': 'Kingston Fury Beast RGB DDR4 32GB (2x16GB) 3600MHz',
                'category': ram_category,
                'description': 'RGB DDR4 memory with infrared sync technology',
                'price': 1999.99,
                'stock': 28,
                'specifications': """32GB total capacity (2x16GB)
DDR4-3600 speed
CL18 latency
1.35V voltage
Intel XMP support
Infrared Sync Technology
RGB lighting
Lifetime warranty"""
            },
            
            # Intel Motherboards
            {
                'name': 'ASUS ROG Maximus Z790 Hero',
                'category': mobo_category,
                'description': 'Premium Z790 motherboard for Intel 13th/14th Gen',
                'price': 8999.99,
                'stock': 8,
                'specifications': """LGA 1700 socket
Intel Z790 chipset
ATX form factor
DDR5 support up to 7800MHz
PCIe 5.0 x16 slot
4x M.2 slots (PCIe 5.0/4.0)
2.5Gb Ethernet
Wi-Fi 6E
USB 3.2 Gen 2x2 Type-C
Aura Sync RGB"""
            },
            {
                'name': 'MSI MAG Z790 Tomahawk WiFi',
                'category': mobo_category,
                'description': 'Feature-rich Z790 board with excellent VRM',
                'price': 5999.99,
                'stock': 12,
                'specifications': """LGA 1700 socket
Intel Z790 chipset
ATX form factor
DDR5 support up to 7200MHz
PCIe 5.0 x16 slot
4x M.2 slots
2.5Gb Ethernet
Wi-Fi 6E
USB 3.2 Gen 2
Mystic Light RGB"""
            },
            {
                'name': 'Gigabyte Z790 AORUS Elite AX',
                'category': mobo_category,
                'description': 'Solid Z790 option with Wi-Fi 6E',
                'price': 4999.99,
                'stock': 15,
                'specifications': """LGA 1700 socket
Intel Z790 chipset
ATX form factor
DDR5 support up to 7600MHz
PCIe 5.0 x16 slot
4x M.2 slots
2.5Gb Ethernet
Wi-Fi 6E
USB 3.2 Gen 2
RGB Fusion 2.0"""
            },
            {
                'name': 'ASRock Z790 Pro RS',
                'category': mobo_category,
                'description': 'Budget-friendly Z790 with essential features',
                'price': 3499.99,
                'stock': 20,
                'specifications': """LGA 1700 socket
Intel Z790 chipset
ATX form factor
DDR5 support up to 6400MHz
PCIe 5.0 x16 slot
3x M.2 slots
2.5Gb Ethernet
USB 3.2 Gen 2
Polychrome RGB"""
            },
            {
                'name': 'ASUS Prime B760-PLUS',
                'category': mobo_category,
                'description': 'Reliable B760 motherboard for mainstream builds',
                'price': 2799.99,
                'stock': 25,
                'specifications': """LGA 1700 socket
Intel B760 chipset
ATX form factor
DDR5 support up to 5333MHz
PCIe 4.0 x16 slot
3x M.2 slots
1Gb Ethernet
USB 3.2 Gen 2
Aura Sync RGB"""
            },
            
            # AMD Motherboards
            {
                'name': 'ASUS ROG Crosshair X670E Hero',
                'category': mobo_category,
                'description': 'Flagship X670E board for AMD Ryzen 7000',
                'price': 9999.99,
                'stock': 6,
                'specifications': """AM5 socket
AMD X670E chipset
ATX form factor
DDR5 support up to 6400MHz
PCIe 5.0 x16 slot
4x M.2 slots (PCIe 5.0/4.0)
2.5Gb Ethernet
Wi-Fi 6E
USB 4.0 support
Aura Sync RGB"""
            },
            {
                'name': 'MSI MAG X670E Tomahawk WiFi',
                'category': mobo_category,
                'description': 'High-performance X670E with great VRM cooling',
                'price': 6499.99,
                'stock': 10,
                'specifications': """AM5 socket
AMD X670E chipset
ATX form factor
DDR5 support up to 6600MHz
PCIe 5.0 x16 slot
4x M.2 slots
2.5Gb Ethernet
Wi-Fi 6E
USB 3.2 Gen 2
Mystic Light RGB"""
            },
            {
                'name': 'Gigabyte B650 AORUS Elite AX',
                'category': mobo_category,
                'description': 'Excellent B650 board with Wi-Fi for Ryzen 7000',
                'price': 3999.99,
                'stock': 18,
                'specifications': """AM5 socket
AMD B650 chipset
ATX form factor
DDR5 support up to 6400MHz
PCIe 4.0 x16 slot
3x M.2 slots
2.5Gb Ethernet
Wi-Fi 6E
USB 3.2 Gen 2
RGB Fusion 2.0"""
            },
            {
                'name': 'ASRock B650M Pro RS',
                'category': mobo_category,
                'description': 'Compact micro-ATX B650 for budget AM5 builds',
                'price': 2499.99,
                'stock': 22,
                'specifications': """AM5 socket
AMD B650 chipset
Micro-ATX form factor
DDR5 support up to 6000MHz
PCIe 4.0 x16 slot
2x M.2 slots
1Gb Ethernet
USB 3.2 Gen 2
Polychrome RGB"""
            },
            {
                'name': 'ASUS TUF Gaming B650-PLUS WiFi',
                'category': mobo_category,
                'description': 'Durable B650 board with military-grade components',
                'price': 3499.99,
                'stock': 16,
                'specifications': """AM5 socket
AMD B650 chipset
ATX form factor
DDR5 support up to 6400MHz
PCIe 4.0 x16 slot
3x M.2 slots
2.5Gb Ethernet
Wi-Fi 6
USB 3.2 Gen 2
Aura Sync RGB"""
            },
        ]
        
        added_count = 0
        for product_data in products:
            slug = slugify(product_data['name'])
            
            # Check if product already exists
            if not Product.objects.filter(slug=slug).exists():
                Product.objects.create(
                    name=product_data['name'],
                    slug=slug,
                    category=product_data['category'],
                    description=product_data['description'],
                    specifications=product_data['specifications'],
                    price=product_data['price'],
                    stock=product_data['stock'],
                    image_url='https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500&h=500&fit=crop'
                )
                added_count += 1
                self.stdout.write(f'Added: {product_data["name"]}')
            else:
                self.stdout.write(self.style.WARNING(f'Already exists: {product_data["name"]}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully added {added_count} new products!'))
