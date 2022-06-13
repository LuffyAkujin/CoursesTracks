!/usr/bin/env python3

import os, sys
from PIL import Image

size = (128, 128)

for infile in os.listdir():
 outfile = os.path.splitext(infile)[0]
 if infile != outfile:
  try:
   with Image.open(infile).convert("RGB") as im:
    im.resize(size)
    im.rotate(270).save("/home/**puttheusername**/opt/icons" + outfile, "JPEG")
  except OSError:
   print("FUCK OFF")
