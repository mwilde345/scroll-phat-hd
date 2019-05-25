#!/usr/bin/env python
from image_load import get_image_data
import time
import scrollphathd
IMAGE_BRIGHTNESS = .6

CAR_1 = get_image_data("./images/car_wheel_1.bmp")
CAR_2 = get_image_data("./images/car_wheel_2.bmp")


def look_down(num):
  if(num==1):
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = CAR_1[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()
  else:
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
      for y in range(0, scrollphathd.DISPLAY_HEIGHT):
          brightness = CAR_1[x][y]
          scrollphathd.pixel(x, y, brightness * IMAGE_BRIGHTNESS)
    scrollphathd.show()

def car():
  scrollphathd.scroll(0,0)
  scrollphathd.show()
  for x in range(51):
      look_down(x%2)
      scrollphathd.scroll(1, 0)
      time.sleep(.01)
      scrollphathd.show()
  scrollphathd.scroll(0,0)
  scrollphathd.clear()
  scrollphathd.show()