import cv2 as cv

img = cv.imread("photos/park.jpg")

# CONVERT TO GRAYSCALE
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# CONVERT TO HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# CONVERT TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)

cv.imshow("parks", lab)
cv.waitKey(0)