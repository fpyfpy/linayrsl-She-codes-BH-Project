#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:49:24 2019

@author: irinasm
"""

from PIL import Image

imgpath = "pic_01.png"


 # My image is a 200x374 jpeg that is 102kb large
img = Image.open(imgpath)
img.show()
print ("Original size:", img.size)


 # I downsize the image with an ANTIALIAS filter (gives the highest quality)
scale_percent = 50   # percent of original size
width = int(img.size[1] * scale_percent / 100)
height = int(img.size[0] * scale_percent / 100)
dim = (width, height)

#img2 = img.resize(dim, Image.ANTIALIAS)
#print ("Resized size:", img2.size)
#img2.show()
img.save("image_scaled.jpg", optimize=True, quality=95)
img3 = Image.open("image_scaled.jpg")
print ("Resized size:", img3.size)

 # The saved downsized image size is 24.8kb
#foo.save("image_scaled_opt.jpg",optimize=True, quality=95)
 # The saved downsized image size is 22.9kb