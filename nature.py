#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:08:39 2019

@author: irinasm
"""







import cv2
import numpy as np
 
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
    
    imgpath = "Nature.jpg"
    imgpath_png = "pic_02.png"
    img = cv2.imread(imgpath)
    img_png = cv2.imread(imgpath_png)
    
    
    cv2.namedWindow("Nature", cv2.WINDOW_AUTOSIZE)
    cv2.startWindowThread()  ###  prosto ne vyvodit' oruginal image na ekran s pom .show()
    
    #display the image
    cv2.imshow('nature_original', img)
    cv2.imshow('pic_02_original', img_png)
 
    # save the image in JPEG format with 85% quality
    outpath_jpeg = "nature_Save_JPEG.jpg"
 
    save(outpath_jpeg, img, jpg_quality=50)
 
    outpath_png = "pic_02_Save_PNG.png"
 
    # save the image in PNG format with 9 Compression
    
    save(outpath_png, img_png, png_compression=9)
 
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        stream.release()
#        cv2.destroyAllWindows()
#        break
#    stream.release()
#    cv2.destroyAllWindows()
#    cv2.waitKey(0)
#    #destroy a certain window
#    cv2.destroyWindow('nature_original')
#    cv2.destroyWindow('pic_02_original')
 
if __name__ == "__main__":
    main()