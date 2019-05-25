#!/usr/bin/env python
from image_load import get_image_data
LOOK_LEFT = list(map(lambda n : "left_"+str(n)+".bmp", range(1,4)))
LOOK_RIGHT = list(map(lambda n : "right_"+str(n)+".bmp", range(1,4)))
LOOK_UP = list(map(lambda n : "up_"+str(n)+".bmp", range(1,4)))
LOOK_DOWN = list(map(lambda n : "down_"+str(n)+".bmp", range(1,4)))
ROLL_EYES = list(map(lambda n : "roll_"+str(n)+".bmp", range(1,14)))
BLINK = list(map(lambda n : "blink_"+str(n)+".bmp", range(1,5)))
def get_eye_data(eye_type):
  eye_data = []
  if eye_type == "left":
    for name in LOOK_LEFT:
      eye_data.append(get_image_data(name))

  if eye_type == "right":
    for name in LOOK_RIGHT:
      eye_data.append(get_image_data(name))

  if eye_type == "up":
    for name in LOOK_UP:
      eye_data.append(get_image_data(name))

  if eye_type == "down":
    for name in LOOK_DOWN:
      eye_data.append(get_image_data(name))

  if eye_type == "roll":
    for name in ROLL_EYES:
      eye_data.append(get_image_data(name))

  if eye_type == "blink":
    for name in BLINK:
      eye_data.append(get_image_data(name))
      
  eye_data.insert(0,get_image_data("neutral.bmp"))
  return eye_data

    