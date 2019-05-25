#!/usr/bin/python
from eye import get_eye_data
import time
import scrollphathd
IMAGE_BRIGHTNESS = .6

LOOK_DOWN = get_eye_data("down")
LOOK_DOWN_REVERSE = LOOK_DOWN[::-1]

for data in LOOK_DOWN:
  for x in range(0, scrollphathd.DISPLAY_WIDTH):
    for y in range(0, scrollphathd.DISPLAY_HEIGHT):
        brightness = data[x][y]
        scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
  scrollphathd.show()
  time.sleep(0.01)
time.sleep(2)
for data in LOOK_DOWN_REVERSE:
  for x in range(0, scrollphathd.DISPLAY_WIDTH):
    for y in range(0, scrollphathd.DISPLAY_HEIGHT):
        brightness = data[x][y]
        scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
  scrollphathd.show()
  time.sleep(0.01)