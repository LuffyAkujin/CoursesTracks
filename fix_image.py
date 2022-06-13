#!/usr/bin/env python
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
 f, e = os.path.splittext(infile)
 outfile = f + ".jpg"
 if infile != outfile:
  try:
   with Image.open(infile) as im:
    im.resize((128, 128))
    im.rotate(-90)
    im.save(outfile)
  except OSError:
   print("Something is wrong cannot convert and resize", infile)
