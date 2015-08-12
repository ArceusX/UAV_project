import regist
import cv2
import numpy

im0 = cv2.imread('/home/triet/Desktop/frames3/frame1.jpg',0)
im1 = cv2.imread('/home/triet/Desktop/frames3/frame2.jpg',0)
im2, scale, angle, (t0, t1) = regist.similarity(im0, im1)
regist.imshow1(im0, im1, im2)
