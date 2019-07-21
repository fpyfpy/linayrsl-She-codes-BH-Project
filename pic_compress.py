#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:43:31 2019

@author: irinasm
"""

import cv2
#import numpy as np
 
def save(path, image, jpg_quality=None, png_compression=None):
  '''
  persist :image: object to disk. if path is given, load() first.
  jpg_quality: for jpeg only. 0 - 100 (higher means better). Default is 95.
  png_compression: For png only. 0 - 9 (higher means a smaller size and longer compression time).
                  Default is 3.
  '''
 
  if jpg_quality:
    cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
  elif png_compression:
    cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
  else:
    cv2.imwrite(path, image)
 
def main():
    
    imgpath = "pic_01.png"
    img = cv2.imread(imgpath)
    print (img.size)
    
    #display the image
    #cv2.imshow('Hanif_Life2Coding', img)
 
    # save the image in JPEG format with 85% quality
    outpath_jpeg = "Hanif_Save_JPEG.jpg"
    save(outpath_jpeg,img,jpg_quality=85)
    bubu1 = cv2.imread(outpath_jpeg)
    print (bubu1.size)
    
    # save the image in PNG format with 4 Compression
    outpath_png = "Hanif_Save_PNG.png"
    save(outpath_png, img,png_compression=4)
    
    bubu = cv2.imread(outpath_png)
    print (img.size, bubu.size)
 
    #cv2.waitKey(0)
    #destroy a certain window
    #cv2.destroyWindow('Hanif_Life2Coding')
 
if __name__ == "__main__":
    main()