#!/usr/bin/python
from eye import get_eye_data
from image_load imporimport time
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