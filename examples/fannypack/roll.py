#!/usr/bin/python
from eye import get_eye_data
import time
import scrollphathd
IMAGE_BRIGHTNESS = .6

ROLL = get_eye_data("roll")
ROLL_REVERSE = ROLL[::-1]

for data in ROLL:
  for x in range(0, scrollphathd.DISPLAY_WIDTH):
    for y in range(0, scrollphathd.DISPLAY_HEIGHT):
        brightness = data[x][y]
        scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
  scrollphathd.show()
  time.sleep(0.01)