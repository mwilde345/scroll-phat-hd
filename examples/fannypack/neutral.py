#!/usr/bin/python
from image_load import get_image_data
import scrollphathd
IMAGE_BRIGHTNESS = .6

NEUTRAL = get_image_data("neutral.bmp")
def neutral():
  for data in NEUTRAL:
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = data[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()