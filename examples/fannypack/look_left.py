#!/usr/bin/python
from eye import get_eye_data
import time
import scrollphathd
IMAGE_BRIGHTNESS = .6

LOOK_LEFT = get_eye_data("left")
LOOK_LEFT_REVERSE = LOOK_LEFT[::-1]
def look_left():
  for data in LOOK_LEFT:
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = data[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()
    time.sleep(0.01)
  time.sleep(2)
  for data in LOOK_LEFT_REVERSE:
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = data[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()
    time.sleep(0.01)