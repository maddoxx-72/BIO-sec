import getpass
import numpy as np
import cv2
import cv2 as cv
import os
import math
import random
import smtplib
from skimage.metrics import structural_similarity as ssim

database = {"name1": "123456", "name2": "1147"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("ma********@gmail.com", "js*************sf")    //Your gmail APP password
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
img = cv.imread('TEST_1.tif')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite('sift_keypoints.jpg',img)
print("finger print matching")
img1 = cv2.imread('TEST_1.tif')
img2 = cv2.imread('sift_keypoints.jpg')

print("Image 1 dimensions:", img1.shape)
print("Image 2 dimensions:", img2.shape)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two images
ssim_score = ssim(gray1, gray2)

print("SSIM:", ssim_score)
if ssim_score < 0.8:
    print("Wrong fingerprint - SSIM score:", ssim_score)
else:
    print("Fingerprints match - SSIM score:", ssim_score)
