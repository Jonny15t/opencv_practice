import cv2 as cv
import numpy as np

img = cv.imread("photos/park.jpg")
b,g,r = cv.split(img)
blank = np.zeros(img.shape[:2], dtype="uint8")
print(blank.shape)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Park", img)
cv.imshow("Park but Red", red)
cv.imshow("Park but Blue", blue)
cv.imshow("Park but Green", green)
cv.waitKey(0)