from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = 'Add detailed specifications to products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding specifications to products...')
        
        specifications = {
            # Laptops
            'MacBook Pro 16"': """16-inch Liquid Retina XDR display
Apple M2 Pro or M3 Pro chip
Up to 96GB unified memory
Up to 8TB SSD storage
Up to 22 hours battery life
Three Thunderbolt 4 ports
HDMI port, SDXC card slot
1080p FaceTime HD camera
Six-speaker sound system with force-cancelling woofers""",

            'Dell XPS 15': """15.6-inch InfinityEdge display (FHD+ or 4K OLED)
12th Gen Intel Core i7 or i9 processor
Up to 64GB DDR5 RAM
Up to 4TB PCIe NVMe SSD
NVIDIA GeForce RTX 3050 Ti graphics
Thunderbolt 4 ports
720p HD webcam
Killer Wi-Fi 6E
Windows 11 Pro""",

            'HP Spectre x360': """13.5-inch 3K2K OLED touchscreen display
12th Gen Intel Core i7 processor
16GB LPDDR4x RAM
1TB PCIe NVMe SSD
Intel Iris Xe graphics
360-degree convertible design
Thunderbolt 4 ports
5MP IR camera with privacy shutter
Bang & Olufsen quad speakers""",

            'Lenovo ThinkPad X1': """14-inch display (FHD or 4K options)
12th Gen Intel Core i5/i7 processor
Up to 32GB LPDDR5 RAM
Up to 2TB PCIe SSD
Intel Iris Xe graphics
MIL-STD-810H tested durability
Thunderbolt 4 ports
1080p webcam with privacy shutter
Dolby Atmos speaker system""",

            'ASUS ROG Zephyrus': """15.6-inch QHD 165Hz display
AMD Ryzen 9 processor
Up to 32GB DDR5 RAM
1TB PCIe 4.0 NVMe SSD
NVIDIA GeForce RTX 4070 graphics
AniMe Matrix LED display
Wi-Fi 6E connectivity
RGB per-key keyboard
Dolby Atmos audio""",

            'Acer Swift 3': """14-inch Full HD IPS display
AMD Ryzen 7 processor
16GB LPDDR4X RAM
512GB NVMe SSD
AMD Radeon graphics
Up to 11.5 hours battery life
Fingerprint reader
Backlit keyboard
Wi-Fi 6 connectivity""",

            'Microsoft Surface Laptop': """13.5-inch PixelSense touchscreen
12th Gen Intel Core i5/i7 processor
8GB or 16GB LPDDR5x RAM
256GB to 1TB SSD
Intel Iris Xe graphics
Alcantara fabric keyboard
720p HD webcam
Omnisonic speakers
Windows 11""",

            # Desktops
            'iMac 24"': """24-inch 4.5K Retina display
Apple M1 chip with 8-core CPU
8GB or 16GB unified memory
256GB to 2TB SSD storage
7-core or 8-core GPU
1080p FaceTime HD camera
Six-speaker sound system
Studio-quality three-mic array
Four USB-C ports (two Thunderbolt)""",

            'Dell Inspiron Desktop': """Intel Core i5 or i7 processor
8GB to 32GB DDR4 RAM
256GB SSD + 1TB HDD
Intel UHD Graphics or NVIDIA GeForce GTX
Multiple USB ports including USB-C
HDMI and DisplayPort outputs
Wi-Fi 6 and Bluetooth 5.0
DVD-RW drive
Windows 11 Home""",

            'HP Pavilion Gaming': """AMD Ryzen 5 or Intel Core i5 processor
8GB to 16GB DDR4 RAM
256GB SSD + 1TB HDD
NVIDIA GeForce GTX 1650 or RTX 3060
Tempered glass side panel
RGB lighting
Wi-Fi 5 and Bluetooth
Multiple USB 3.0 ports
Windows 11""",

            'Alienware Aurora': """12th Gen Intel Core i7 or i9 processor
16GB to 64GB DDR5 RAM
512GB to 2TB NVMe SSD
NVIDIA GeForce RTX 3070 to RTX 4090
AlienFX RGB lighting
Liquid cooling system
Killer Wi-Fi 6E
Tool-less upgradability
Windows 11""",

            'ASUS ROG Strix': """AMD Ryzen 9 or Intel Core i9 processor
32GB to 64GB DDR5 RAM
1TB to 2TB NVMe SSD
NVIDIA GeForce RTX 4080 or 4090
Aura Sync RGB lighting
360mm AIO liquid cooler
Wi-Fi 6E connectivity
Tempered glass panel
Windows 11 Pro""",

            'Lenovo IdeaCentre': """Intel Core i5 or i7 processor
8GB to 16GB DDR4 RAM
512GB SSD
Intel UHD Graphics
Compact tower design
Multiple USB ports
HDMI output
Wi-Fi 6 and Bluetooth
Windows 11 Home""",

            # Monitors
            'LG UltraGear 27"': """27-inch QHD (2560x1440) display
144Hz refresh rate
1ms response time (GtG)
NVIDIA G-SYNC compatible
HDR10 support
99% sRGB color gamut
AMD FreeSync Premium
Tilt, height, pivot adjustable stand
HDMI 2.0 and DisplayPort 1.4""",

            'Samsung Odyssey G7': """32-inch QLED curved display
2560x1440 resolution
240Hz refresh rate
1ms response time
1000R curvature
NVIDIA G-SYNC and AMD FreeSync
HDR600 support
Height and tilt adjustable
HDMI 2.0 and DisplayPort 1.4""",

            'Dell UltraSharp 32"': """32-inch 4K UHD (3840x2160) display
IPS Black technology
60Hz refresh rate
99% sRGB, 95% DCI-P3 color coverage
USB-C hub with 90W power delivery
Built-in KVM switch
Height, tilt, swivel, pivot adjustable
HDMI, DisplayPort, USB-C connectivity""",

            'ASUS ProArt Display': """27-inch 4K UHD (3840x2160) display
IPS panel with 100% sRGB, 100% Rec. 709
Delta E < 2 color accuracy
Calman verified and factory calibrated
USB-C with 96W power delivery
Ergonomic stand with full adjustability
HDMI, DisplayPort, USB-C ports
Built-in color uniformity technology""",

            'BenQ PD2700U': """27-inch 4K UHD IPS display
100% sRGB and Rec. 709 color space
CAD/CAM and Animation modes
Darkroom mode for photo editing
Dual view mode
USB-C connectivity with 65W power delivery
Height, tilt, swivel, pivot adjustable
HDMI, DisplayPort, USB-C""",

            'Acer Predator X34': """34-inch curved ultrawide display
3440x1440 resolution
180Hz refresh rate (overclocked)
1ms VRB response time
NVIDIA G-SYNC compatible
HDR400 support
Height, tilt, swivel adjustable
HDMI 2.0 and DisplayPort 1.4""",

            'ViewSonic VP2468': """24-inch Full HD (1920x1080) display
IPS panel with 178° viewing angles
100% sRGB color accuracy
Hardware calibration support
Ergonomic stand with full adjustability
Flicker-free and blue light filter
HDMI, DisplayPort, USB-C
Built-in USB 3.0 hub""",

            # Keyboards
            'Logitech MX Keys': """Full-size wireless keyboard
Backlit keys with smart illumination
Spherically-dished keys
Multi-device connectivity (up to 3 devices)
USB-C rechargeable battery
Up to 10 days battery life (backlit)
Compatible with Windows, macOS, Linux
Logitech Flow technology
Bluetooth and USB receiver""",

            'Corsair K95 RGB': """Mechanical gaming keyboard
Cherry MX Speed switches
Per-key RGB backlighting
6 dedicated macro keys
Detachable soft-touch wrist rest
Dedicated media controls
USB pass-through port
Aircraft-grade aluminum frame
iCUE software compatible""",

            'Razer BlackWidow V3': """Mechanical gaming keyboard
Razer Green mechanical switches
Chroma RGB backlighting
Doubleshot ABS keycaps
Ergonomic wrist rest included
Dedicated media keys
USB pass-through
Aluminum construction
Razer Synapse 3 compatible""",

            'Keychron K8': """Wireless mechanical keyboard
Hot-swappable switches
Mac and Windows compatible
RGB or white backlight options
Bluetooth 5.1 connectivity
Up to 240 hours battery life
Aluminum frame
Gateron mechanical switches
Compact tenkeyless design""",

            'SteelSeries Apex Pro': """Mechanical gaming keyboard
OmniPoint adjustable switches
OLED smart display
Aircraft-grade aluminum frame
Magnetic wrist rest
Dedicated media controls
USB pass-through
Per-key RGB illumination
SteelSeries Engine software""",

            'Das Keyboard 4': """Professional mechanical keyboard
Cherry MX switches (multiple options)
Two-port USB 3.0 hub
Dedicated media controls
Oversized volume knob
Aluminum top panel
Soft-touch magnetic footbar
N-key rollover
Gold-plated mechanical switches""",

            # Mice
            'Logitech MX Master 3': """Wireless ergonomic mouse
4000 DPI Darkfield sensor
MagSpeed electromagnetic scrolling
Multi-device connectivity (up to 3)
USB-C rechargeable battery
Up to 70 days on full charge
Customizable buttons
Logitech Flow technology
Works on any surface including glass""",

            'Razer DeathAdder V3': """Ergonomic gaming mouse
Focus Pro 30K optical sensor
Up to 30,000 DPI
Razer Optical Mouse Switches Gen-3
63g lightweight design
Razer HyperSpeed wireless
Up to 90 hours battery life
8 programmable buttons
Razer Synapse 3 compatible""",

            'Logitech G Pro X': """Wireless gaming mouse
HERO 25K sensor
Up to 25,600 DPI
LIGHTSPEED wireless technology
POWERPLAY compatible
60 hours battery life
Zero additive PTFE feet
5 programmable buttons
Lightweight 63g design""",

            'Corsair Dark Core RGB': """Wireless gaming mouse
18,000 DPI optical sensor
Qi wireless charging compatible
Bluetooth and 2.4GHz wireless
Interchangeable side grips
9 programmable buttons
RGB lighting zones
Up to 50 hours battery life
iCUE software compatible""",

            'SteelSeries Rival 3': """Gaming mouse
TrueMove Core 8,500 CPI sensor
6 programmable buttons
Brilliant Prism RGB lighting
Split-trigger buttons
Durable mechanical switches
60 million click durability
Lightweight 77g design
SteelSeries Engine software""",

            'Razer Basilisk V3': """Ergonomic gaming mouse
Focus+ 26K DPI optical sensor
11 programmable buttons
Razer HyperScroll tilt wheel
Chroma RGB with 11 lighting zones
Optical mouse switches Gen-2
Customizable scroll wheel resistance
Ergonomic thumb rest
Razer Synapse 3 compatible""",

            # Headphones
            'Sony WH-1000XM5': """Industry-leading noise cancellation
30-hour battery life
Multipoint connection
Speak-to-chat technology
Adaptive Sound Control
LDAC, AAC, SBC codec support
Touch sensor controls
Comfortable lightweight design
Carrying case included""",

            'Bose QuietComfort 45': """World-class noise cancellation
24-hour battery life
TriPort acoustic architecture
Adjustable EQ in Bose Music app
Aware Mode for ambient sound
Bluetooth 5.1 connectivity
Lightweight and comfortable
Foldable design with case
USB-C charging""",

            'SteelSeries Arctis 7': """Wireless gaming headset
2.4GHz lossless wireless
24-hour battery life
DTS Headphone:X v2.0 surround
ClearCast bidirectional microphone
On-headset controls
Ski goggle suspension headband
Compatible with PC, PlayStation, Switch
SteelSeries Engine software""",

            'HyperX Cloud II': """Gaming headset
53mm drivers
7.1 virtual surround sound
Detachable noise-cancelling microphone
Memory foam ear cushions
Aluminum frame
In-line audio control
Compatible with PC, PS4, Xbox
Durable braided cable""",

            'Razer BlackShark V2': """Esports gaming headset
Razer TriForce 50mm drivers
THX Spatial Audio
Detachable HyperClear cardioid mic
Advanced passive noise cancellation
Memory foam ear cushions
Lightweight 262g design
3.5mm jack connectivity
Razer Synapse 3 compatible""",

            'Audio-Technica ATH-M50x': """Professional studio monitor headphones
45mm large-aperture drivers
Exceptional clarity and deep bass
90° swiveling earcups
Detachable cables (3 included)
Professional-grade ear pads
Collapsible design
Carrying pouch included
Frequency response: 15-28,000 Hz""",

            # Webcams
            'Logitech C920': """1080p Full HD video at 30fps
Carl Zeiss optics
Autofocus technology
Dual stereo microphones
78° field of view
Automatic light correction
Universal clip design
USB-A connectivity
Compatible with Windows, macOS, Chrome OS""",

            'Razer Kiyo Pro': """1080p 60fps video
Adaptive light sensor
Wide-angle lens
Uncompressed video
HDR enabled
Advanced autofocus
Built-in adjustable ring light
USB 3.0 connectivity
Razer Synapse compatible""",

            'Logitech Brio 4K': """4K Ultra HD at 30fps or 1080p at 60fps
5x digital zoom
HDR support
RightLight 3 with HDR
90° field of view
Infrared sensor for Windows Hello
Dual omnidirectional microphones
USB 3.0 connectivity
Privacy shutter included""",

            'Elgato Facecam': """1080p 60fps uncompressed video
Sony STARVIS CMOS sensor
Fixed focus optics
82° field of view
Advanced image engine
USB 3.0 connectivity
Elgato Camera Hub software
Professional mounting options
Privacy shutter""",

            'Microsoft LifeCam HD': """720p HD video
TrueColor technology
Wideband microphone
Universal attachment base
Auto focus
USB 2.0 connectivity
Compatible with Windows
Skype certified
Compact design""",

            # Speakers
            'Logitech Z623': """2.1 speaker system
200 watts RMS power
THX certified audio
Dual RCA and 3.5mm inputs
On-speaker controls
Ported, down-firing subwoofer
Satellite speakers with wall-mount option
Headphone jack
Compatible with PC, TV, game consoles""",

            'Bose Companion 2': """2.0 speaker system
Proprietary TrueSpace technology
Ported cabinet design
Volume control on right speaker
Auxiliary input
Headphone jack
Compact desktop design
Single connection to computer
Clear, natural sound""",

            'Audioengine A2+': """Powered desktop speakers
60W peak power
Built-in 24-bit DAC
Bluetooth aptX connectivity
RCA, USB, and 3.5mm inputs
Subwoofer output
Aramid fiber woofers
Silk dome tweeters
Remote control included""",

            'Creative Pebble V3': """2.0 USB-C powered speakers
8W RMS power
Minimalist spherical design
45° elevated drivers
Rear-facing passive radiator
Gain control knob
USB-C and 3.5mm connectivity
Clear Dialog audio enhancement
Compact desktop footprint""",

            'Razer Nommo Chroma': """2.0 gaming speakers
Custom woven glass fiber drivers
Rear-facing bass ports
Automatic gain control
Razer Chroma RGB lighting
Volume and bass control knobs
3.5mm and USB connectivity
Razer Synapse compatible
Weighted bases for stability""",

            # Graphics Cards
            'NVIDIA RTX 4090': """24GB GDDR6X memory
16384 CUDA cores
2.52 GHz boost clock
Ada Lovelace architecture
Ray tracing cores (3rd gen)
Tensor cores (4th gen)
DLSS 3 support
PCIe 4.0 interface
450W TDP""",

            'NVIDIA RTX 4080': """16GB GDDR6X memory
9728 CUDA cores
2.51 GHz boost clock
Ada Lovelace architecture
Ray tracing cores (3rd gen)
Tensor cores (4th gen)
DLSS 3 support
PCIe 4.0 interface
320W TDP""",

            'NVIDIA RTX 4070 Ti': """12GB GDDR6X memory
7680 CUDA cores
2.61 GHz boost clock
Ada Lovelace architecture
Ray tracing cores (3rd gen)
Tensor cores (4th gen)
DLSS 3 support
PCIe 4.0 interface
285W TDP""",

            'AMD Radeon RX 7900 XTX': """24GB GDDR6 memory
6144 stream processors
2.5 GHz boost clock
RDNA 3 architecture
96 Ray Accelerators
96 AI Accelerators
DisplayPort 2.1 support
PCIe 4.0 interface
355W TDP""",

            'NVIDIA RTX 4060 Ti': """8GB or 16GB GDDR6 memory
4352 CUDA cores
2.54 GHz boost clock
Ada Lovelace architecture
Ray tracing cores (3rd gen)
Tensor cores (4th gen)
DLSS 3 support
PCIe 4.0 interface
160W TDP""",

            'AMD Radeon RX 7800 XT': """16GB GDDR6 memory
3840 stream processors
2.43 GHz boost clock
RDNA 3 architecture
60 Ray Accelerators
60 AI Accelerators
DisplayPort 2.1 support
PCIe 4.0 interface
263W TDP""",

            # Processors
            'Intel Core i9-14900K': """24 cores (8P + 16E)
32 threads
Up to 6.0 GHz max turbo
36MB Intel Smart Cache
125W base power
LGA 1700 socket
DDR5-5600 support
PCIe 5.0 and 4.0 support
Intel UHD Graphics 770""",

            'AMD Ryzen 9 7950X': """16 cores
32 threads
Up to 5.7 GHz boost clock
80MB total cache
170W TDP
AM5 socket
DDR5-5200 support
PCIe 5.0 support
Integrated RDNA 2 graphics""",

            'Intel Core i7-14700K': """20 cores (8P + 12E)
28 threads
Up to 5.6 GHz max turbo
33MB Intel Smart Cache
125W base power
LGA 1700 socket
DDR5-5600 support
PCIe 5.0 and 4.0 support
Intel UHD Graphics 770""",

            'AMD Ryzen 7 7800X3D': """8 cores
16 threads
Up to 5.0 GHz boost clock
104MB total cache (with 3D V-Cache)
120W TDP
AM5 socket
DDR5-5200 support
PCIe 5.0 support
Integrated RDNA 2 graphics""",

            'Intel Core i5-14600K': """14 cores (6P + 8E)
20 threads
Up to 5.3 GHz max turbo
24MB Intel Smart Cache
125W base power
LGA 1700 socket
DDR5-5600 support
PCIe 5.0 and 4.0 support
Intel UHD Graphics 770""",

            'AMD Ryzen 5 7600X': """6 cores
12 threads
Up to 5.3 GHz boost clock
38MB total cache
105W TDP
AM5 socket
DDR5-5200 support
PCIe 5.0 support
Integrated RDNA 2 graphics""",
        }
        
        updated_count = 0
        for product_name, specs in specifications.items():
            try:
                product = Product.objects.get(name=product_name)
                product.specifications = specs
                product.save()
                updated_count += 1
                self.stdout.write(f'Updated specifications for: {product_name}')
            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Product not found: {product_name}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} product specifications!'))
