import cv2 as cv
import numpy as np

img = cv.imread("photos/cats.jpg")
blank = np.zeros(img.shape, dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
edges = cv.Canny(blur, 125, 175)

# THRESHOLD TRIES TO BINARIZE AN IMAGE, BLACK OR WHITE
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, heirarchies = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} countour(s) found!")

cv.drawContours(blank, contours, -1, (0,0,255), thickness=1)

cv.imshow("Blank", blank)
cv.imshow("Cats", gray)
cv.waitKey(0)