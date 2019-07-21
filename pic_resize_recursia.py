#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:18:38 2019

@author: irinasm
"""
    
    
img1_path = "grass.jpg"
img2_path = "pic_01.png"

img1 = cv2.imread(img1_path, cv2.IMREAD_UNCHANGED)  # loading image from file
img2 = cv2.imread(img2_path, cv2.IMREAD_UNCHANGED)

scale_percent = 50   # percent of original size
jpg_quality = 90
png_compression = 9
# max_size = 2000000  

width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)

# Picture resizing by changing image resolution  
img1_resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)  # INTER_AREA - resampling using pixel area relation

# Printing is only for checking, will be deleted
print ("Original Dimensions:", img1.shape)
print ("Original Size:", img1.size)
print ("Resized Dimensions:", img1_resized.shape)
print ("Resized Size:", img1_resized.size)
print ()

# Picture resizing by changing image quality 
outpath_jpeg = "Save_JPEG.jpg"
result1, img1_encode = cv2.imencode(outpath_jpeg, img1_resized, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])

# Printing is only for checking, will be deleted
print ("Original Size:", img1.size, img1_resized.size)
print ("Compressed with 90% QUALITY:", img1_encode.size)


outpath_png = "Save_PNG.png"
result2, img2_encode = cv2.imencode(outpath_png, img2, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
print ("Original Size:", img2.size)
print ("Compressed with 9 QUALITY:", img2_encode.size)







### Picture resize ###

import cv2
#import opencv

 
my_img = cv2.imread("grass.jpg", cv2.IMREAD_UNCHANGED)
my_scale_percent = 50   # percent of original size
max_size = 2000000  
  # INTER_AREA - resampling using pixel area relation
  

def resize(img, scale_percent):
    print ("Original Dimensions:", img.shape)
    print ("Original Size:", img.size)
    
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    if img.size <= max_size:
        print ("Resized Dimensions:", resized.shape)
        print ("Resized Size:", resized.size)
        return 0
    return resize(img, (scale_percent/???))

resize(my_img, my_scale_percent)

## Compressing -- ne poluchilos'

#cv2.imwrite('compress_img.jpg', resized,  (cv2.IMWRITE_PNG_COMPRESSION, 9))
#img2 = cv2.imread('compress_img.jpg', cv2.IMREAD_UNCHANGED)
#print ("Compressed:", img2.size)

## Izobrazhenie image i udalenie ego okna - ne rabotaet Destroy
##cv2.imshow("Resized image" , resized)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##cv2.waitKey(1)


#cv2.imwrite('compress_img.jpg', img,  (cv2.IMWRITE_PNG_COMPRESSION, 9))
#img2 = cv2.imread('compress_img.jpg', cv2.IMREAD_UNCHANGED)
#
#
##result, encimg = cv2.imencode('01.png', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
#
#
##print('Dimensions : ',img.size, img2.size)
#print("--------------")
#print('Original Dimensions : ',img.size)
#print('Compressed Dimensions : ',img2.size)