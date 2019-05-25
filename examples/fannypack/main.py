#!/usr/bin/env python
import scrollphathd

from eye_seq import eye_seq
from car import car
from myclock import myclock
from jokes import jokes
from amazon import amazon

seq = ["eye_seq","car","myclock","jokes","jokes","amazon"]
fileMap = {
  "eye_seq": eye_seq,
  "car": car,
  "myclock": myclock,
  "jokes": jokes,
  "amazon": amazon
}
try:
  while True:
    item = random.choice(seq)
    fileMap[item]()
    time.sleep(random.randint(1,3))
except KeyboardInterrupt:
  scrollphathd.fill(0)
  scrollphathd.show()
