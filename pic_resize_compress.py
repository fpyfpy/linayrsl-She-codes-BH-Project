#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:15:09 2019

@author: irinasm
"""

### Picture Resize and Compress

import cv2
#import opencv
import base64
import numpy as np
import os


def resizeImg(image, scale_percent):
  """
  Resize image by changing its resolution
  """
  max_size = 2000000           # sdelat' global const?
  min_dimensions = (600, 400)  # sdelat' global const?
  width = int(image.shape[1] * scale_percent / 100)
  height = int(image.shape[0] * scale_percent / 100)
  dimensions = (width, height)

  print ("Original Dimensions:", image.shape)
  print ("Original Size:", image.size)
 
  while image.size > max_size and dimensions > min_dimensions:
      image_resized = cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA)  # INTER_AREA - resampling using pixel area relation
      dimensions = int(dimensions[0]/2), int(dimensions[1]/2)
      image = image_resized
      
  # Printing is only for checking, will be deleted
  print ("Resized Dimensions:", image.shape)
  print ("Resized Size:", image.size)
  print ()
  
  return image
  

def saveImg(path, image, jpg_quality = None, png_compression = None):
  """
  Save image with determined quality/compression
  image: object to compressing, path: filename to save
  jpg_quality: for jpeg only, 0 - 100 (higher means better). Default is 95.
  png_compression: For png only, 0 - 9 (higher means a smaller size and longer compression time).
                  Default is 3.
  """
  if jpg_quality:
      cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
  elif png_compression:
      cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
  else:
      cv2.imwrite(path, image)  # another picture format - what to do? --- ???
  return 0    


def toByteString(image, path):
#  """
#  Convert image to text data
#  image: object to converting, path: filename to save image like text data
#  cv2.imencode() function is to convert (encode) the image format into streaming data and assign it to memory cache.
#  It is mainly used for compressing image data format to facilitate network transmission.
#  """
    image_readed = cv2.imread(image, cv2.IMREAD_UNCHANGED)  # loading jpg_image from the file

    # Convert image to streaming data
    result, buffer = cv2.imencode(path, image_readed)

    # Convert to base64 encoding and show start of data
    image_as_text = base64.b64encode(buffer)
    print("image_as_text:", image_as_text[:80])  # Print 80 first bytes. Printing is only for checking, will be deleted
    return image_as_text


def fromByteString(image_as_text):
#  """
#  Convert text data (converted image) to JPG file
#  image_as_text: converted object
#  cv2.imdecode() function reads data from specified memory cache and converts (decodes) data into image format;
#  it is mainly used to recover images from network transmission data.
#  """
    # Convert back to binary
    image_original = base64.b64decode(image_as_text)
    #print ("jpg_original:", jpg_original)   # to long. Printing is only for checking, will be deleted

    # Write to a file to show conversion worked
    with open('nature_back.jpg', 'wb') as file_output:
        file_output.write(image_original)
    return 0    
    
    
def main():
    scale_percent = 50   # percent of original size
    jpg_quality = 90
    png_compression = 9
   # global max_size
   # max_size = 2000000
    
    img_jpg_path = "grass.jpg"
    img_png_path = "simpson.png"
    
    img_jpg = cv2.imread(img_jpg_path, cv2.IMREAD_UNCHANGED)  # loading jpg_image from the file
    img_png = cv2.imread(img_png_path, cv2.IMREAD_UNCHANGED)  # loading png_image from the file
    
    print ("jpg")     # Printing is only for checking, will be deleted
    outpath_jpg = "save_JPG.jpg"
    saveImg(outpath_jpg, resizeImg(img_jpg, scale_percent), jpg_quality, None)
    print ("Compressed with %d percent QUALITY:" % jpg_quality, os.path.getsize(outpath_jpg)) # Printing is only for checking, will be deleted
    print ()          # Printing is only for checking, will be deleted
    print ("png")     # Printing is only for checking, will be deleted
    outpath_png = "save_PNG.png"
    saveImg(outpath_png, resizeImg(img_png, scale_percent), None, png_compression)
    print ("Compressed with %d COMPRESSION:" % png_compression, os.path.getsize(outpath_png)) # Printing is only for checking, will be deleted
    print ()          # Printing is only for checking, will be deleted
    
    img_path = "nature.jpg"
    path_encode = ".jpg"
    nature_text = toByteString(img_path, path_encode)
    fromByteString(nature_text)
    
    
if __name__ == "__main__":
    main()