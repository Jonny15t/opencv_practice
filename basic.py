import cv2 as cv

img = cv.imread("photos/lady.jpg")

# CONVERT IMAGE TO GRAYSCALE
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# BLUR AN IMAGE
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# EDGE CASCADE
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

# DILATE THE EDGES
# dilated = cv.dilate(canny, (12,12), iterations=2)
# cv.imshow("Dilated", dilated)

# ERODING THE EDGES
# eroded = cv.erode(dilated, (4,4), iterations=2)
# cv.imshow("Eroded", eroded)

# RESIZE AN IMAGE
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow("Resized", resized)

# CROPPING
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

# cv.imshow("Lady", img)
cv.waitKey(0)