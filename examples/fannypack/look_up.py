#!/usr/bin/python
from eye import get_eye_data
import time
import scrollphathd
IMAGE_BRIGHTNESS = .6

LOOK_UP = get_eye_data("up")
LOOK_UP_REVERSE = LOOK_UP[::-1]
def look_up():
  for data in LOOK_UP:
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = data[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()
    time.sleep(0.01)
  time.sleep(2)
  for data in LOOK_UP_REVERSE:
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = data[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()
    time.sleep(0.01)