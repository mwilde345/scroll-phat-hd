## Hello!
This is a random and crazy idea I had.
I wanted to put an LED matrix on a fannypack.

I first tried with the Sunfounder EMO 24x8, but the device didn't work correctly.

I wanted safe shutdown for the pi while carrying the pack around, so I got the pimoroni on/off shim. It works great, but I screwed up bad while soldering and broke it.

I ended up going with a little 3.7V arduino Li-Ion battery, hooked up to the juicebox Zero (rigged a manual safe shutdown button), and attached that to the Pi Zero and then wired on the pimoroni scroll phat hd.

This can be powered by the Li-Ion battery or a portable usb battery pack.

The main.py file runs a random set of other scripts to do cool things on the led matrix.

Went on vacation with it and some people asked about it. Will probably just take it apart now.