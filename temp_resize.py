#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 01:44:31 2019

@author: irinasm
"""
import cv2

#cv2.imdecode() function reads data from specified memory cache and converts (decodes) data into image format;
#it is mainly used to recover images from network transmission data.
#cv2.imencode() function is to convert (encode) the image format into streaming data and assign it to memory cache.
#It is mainly used for compressing image data format to facilitate network transmission


## Izobrazhenie image i udalenie ego okna - ne rabotaet Destroy
##cv2.imshow("Resized image" , resized)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##cv2.waitKey(1)
###cv2.imshow("Compressed image" , img_encode)

# if jpg_quality:
#      ##result, image_encode = cv2.imencode(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
#      cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
#  elif png_compression:
#      ##result, image_encode = cv2.imencode(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
#      cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
#  else:
#      cv2.imwrite(path, image)  # another picture format - what to do? --- ???
#   
 
#If you have an image img (which is a numpy array) you can convert it into string using:
#
#>>> img_str = cv2.imencode('.jpg', img)[1].tostring()
#>>> type(img_str)
# 'str'
#Now you can easily store the image inside your database, and then recover it by using:
#
#>>> nparr = np.fromstring(STRING_FROM_DATABASE, np.uint8)
#>>> img = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
#where you need to replace STRING_FROM_DATABASE with the variable that contains the result of your query to the database containing the image.   
#    

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

img2_resized = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
print ("Original Size:", img2.size)
print ("Resized Size:", img2_resized.size)
outpath_png = "Save_PNG.png"
result2, img2_encode = cv2.imencode(outpath_png, img2_resized, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
print ("Original Size:", img2.size)
print ("Compressed with 9 QUALITY:", img2_encode.size)

print (img1_encode)
result1, img1_encode = cv2.imencode(outpath_jpeg, img1_resized, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
img1_decode = cv2.imdecode(img1_encode, cv2.IMREAD_UNCHANGED)
print (img1_decode)
print ("---------")


import base64

image = cv2.imread("nature.jpg", cv2.IMREAD_UNCHANGED)

# Convert captured image to JPG
retval, buffer = cv2.imencode('.jpg', image) #return value

# Convert to base64 encoding and show start of data
jpg_as_text = base64.b64encode(buffer)
print("jpg_as_text:", jpg_as_text[:80])

# Convert back to binary
jpg_original = base64.b64decode(jpg_as_text)
#print ("jpg_original:", jpg_original) # dlinno

# Write to a file to show conversion worked
with open('nature_back.jpg', 'wb') as f_output:
    f_output.write(jpg_original)