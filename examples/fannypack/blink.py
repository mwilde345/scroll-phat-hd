#!/usr/bin/python
from eye import get_eye_data
import time
import scrollphathd
IMAGE_BRIGHTNESS = .6

BLINK = get_eye_data("blink")
BLINK_REVERSE = BLINK[::-1]

def blink():
  for data in BLINK:
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = data[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()
    time.sleep(0.001)
  time.sleep(.002)
  for data in BLINK_REVERSE:
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = data[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()
    time.sleep(0.005)