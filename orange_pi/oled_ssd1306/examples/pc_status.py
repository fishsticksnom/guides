import time
import psutil as PS
from oled.device import ssd1306
from oled.render import canvas
from PIL import Image, ImageFont, ImageDraw

bitmap_font = "Vermin Vibes 1989.ttf"
# bitmap_font='C&C Red Alert [INET].ttf'
# bitmap_font='Volter__28Goldfish_29.ttf'

KB = 1024
MB = KB * 1024
GB = MB * 1024

device = ssd1306(port=3, address=0x3C)

while True:
    CPU = "CPU {:.1f}%".format(round(PS.cpu_percent(), 1))

    temps = PS.sensors_temperatures()
    TEMP = "{:.1f} C".format(round(temps["cpu_thermal"][0].current, 1))

    mem = PS.virtual_memory()
    MemUsage = "RAM {:5d}/{:5d} MB".format(
        round((mem.used + MB - 1) / MB), round((mem.total + MB - 1) / MB)
    )

    root = PS.disk_usage("/")
    Disk = "HDD {:4d} / {:4d} GB".format(
        round((root.used + GB - 1) / GB), round((root.total + GB - 1) / GB)
    )

    with canvas(device) as draw:
        # font = ImageFont.load_default()
        font = ImageFont.truetype("./fonts/" + bitmap_font, 16)
        logo = Image.open("./images/larva01.png")
        draw.bitmap((80, -19), logo, fill=1)
        draw.text((0, 0), CPU, font=font, fill=255)
        draw.text((0, 14), "TEMP " + TEMP, font=font, fill=255)
        draw.text((0, 28), MemUsage, font=font, fill=255)
        draw.text((0, 42), Disk, font=font, fill=255)

    time.sleep(1.0)
