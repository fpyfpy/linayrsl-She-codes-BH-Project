#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:38:12 2019

@author: irinasm
"""

"""
Resizing, Compressing, Transforming image JPG/PNG
"""

import cv2

class ImageTransform(object):
    def __init__(self, id, firstName = "unknown",
                          ):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate

        
    def setID(self):
        
        
        
        

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
    