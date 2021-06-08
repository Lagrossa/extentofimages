import PIL
import random
from PIL import Image
# SO... we want to create a file which displays an image, with... 
# each pixel having a random RGB value
# how stupid of an idea would it be to iterate through and modify all 2,073,600 pixels..?
color_random = (0,0,0)
color_value1 = 0
color_value2 = 0
color_value3 = 0

def randomColor():
    color_random = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    return (color_random)

image_display = PIL.Image.new("RGB", (1920, 1080))

#coordinates
width = image_display.width
height = image_display.height
x = 0
y = 0

for x in range(0,width):
    for y in range(0,height):
        image_display.putpixel((x,y),(color_value1,color_value2,color_value3))
        color_value1 += 1
        color_value2 += 1
        color_value3 += 1


image_display.show()

print("wait holy shit that actually works LMAOOO")