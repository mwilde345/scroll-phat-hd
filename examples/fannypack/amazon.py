#!/usr/bin/python
from image_load import get_image_data
import scrollphathd
import time
IMAGE_BRIGHTNESS = .6

AMZN = get_image_data("amazon.bmp")
AMZN_NEG = get_image_data("amazon_negative.bmp")
def amazon():
  for z in range(8):
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = NEUTRAL[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()
    time.sleep(.5)
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = NEUTRAL[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()
    time.sleep(.5)