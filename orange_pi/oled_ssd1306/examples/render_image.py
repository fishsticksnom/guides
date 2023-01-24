#!/usr/bin/env python

import time
from oled.device import ssd1306
from oled.render import canvas
from PIL import Image

# Instructions:
# If you like to display an image or a gif in your oled you will need to convert
# it into a bmp format.

# Steps

# 1.Go https://onlineimagetools.com/convert-gif-to-bmp
# 2.Upload image
# 3.Select Frame Options: (frame 1)
# 4.Select Chain with: (Resize Bitmap width 128 height 64)
# 5.Select Chain with: (Create a Transparent Bitmap: Color to Match: black "the images only work when the colors are black and white")
# 6. Save as
# 7.Downlaod
# 8.Rename image: ("If the frame is 1 save it as nameoftheimage01.png if is frame 2 save it as nameoftheimage02.png")
# 9.Repeat for each frame


device = ssd1306(port=3, address=0x3C)

# Display the gif 10 times.
gif_times = 10

# If your gif has 10 frames add them in the list below.
frames = ["01", "02", "03", "04"]


def gif():
    for x in range(gif_times):
        for frame in frames:
            with canvas(device) as draw:
                # Chage larva for your image.
                logo = Image.open(f"./images/larva{frame}.png")
                draw.bitmap((30, 0), logo, fill=1)
                time.sleep(0.1)  # Speed of the animation
                if x == gif_times - 1:
                    draw.bitmap((30, 0), logo, fill=0)  # Clean screen after 10 times.


def single_image():
    with canvas(device) as draw:
        logo = Image.open(
            "./images/larva01.png"
        )  # Change the name of the image to display.
        draw.bitmap((30, 0), logo, fill=1)


gif()
# single_image()
