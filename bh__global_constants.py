#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:45:11 2019

@author: irinasm
"""

"""
Global constants
"""

class ImageConst(object):
   def __init__(self, max_size = 0,
                       min_dimensions = (0,0),
                       scale_percent = 100,
                       jpg_quality = 100,
                       png_compression = 0):
        
        self.max_size = max_size,
        self.min_dimensions = min_dimensions
        self.scale_percent = scale_percent   # percent of original size
        self.jpg_quality = jpg_quality
        self.png_compression = png_compression 
      
   def setMaxSize(self):
      self.max_size = 2000000
      
   def setMinDimensions(self):
       self.min_dimensions = (600,400)
          
   def setScalePercent(self):
       self.scale_percent = 50
        
   def setJpgQuality(self):
       self.jpg_quality = 90
        
   def setJpgQuality(self):
       self.png_compression = 9
        
   def setData(self):
       self.setMaxSize()
       self.setMinDimensions()
       self.setScalePercent()
       self.setJpgQuality()
       self.setJpgQuality()
       return 1

   def __print__(self):
       #min_dimensions = %(d,d), self.min_dimensions)
       print ("max_size = %d" % self.max_size)
       print ("scale_percent = %d, jpg_quality = %d, png_compression = %d" %(self.scale_percent, self.jpg_quality, self.png_compression))

my_image = ImageConst()
my_image.setData()
my_image.__print__()