#!/usr/bin/python
import random
import time

from blink import blink
from neutral import neutral
from look_down import look_down
from look_left import look_left
from look_right import look_right
from look_up import look_up
from roll import roll

seq = ["blink","look_left","look_right","look_up","look_down","roll"]
fileMap = {
  "blink": blink,
  "look_left": look_left,
  "look_right": look_right,
  "look_up": look_up,
  "look_down": look_down,
  "roll": roll
}

for x in range(20):
  item = random.choice(seq)
  fileMap[item]()
  neutral()
  time.sleep(random.randint(1,4))
