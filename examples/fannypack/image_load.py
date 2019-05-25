#!/usr/bin/env python
try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

IMAGE_BRIGHTNESS = 0.5
img = None

def set_img_var(filename):
  global img
  img = Image.open("./images/"+filename)

def get_pixel(x, y):
  p = img.getpixel((x, y))
  if img.getpalette() is not None:
      r, g, b = img.getpalette()[p:p + 3]
      p = max(r, g, b)
  else:
    p = max(p)
  return p / 255.0

def get_image_data(filename):
  set_img_var(filename)
  image_data = []
  for x in range(0, 17):
    y_data = []
    for y in range(0, 7):
      y_data.append(get_pixel(x, y))
    image_data.append(y_data)
  return image_data

