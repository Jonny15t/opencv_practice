import cv2 as cv
import numpy as np

img = cv.imread("photos/lady.jpg")

# TRANSLATE
# def translate(img, x, y):
#     translationMatrix = np.float32([[1,0,x], [0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, translationMatrix, dimensions)

# translated = translate(img, -100, 100)
# cv.imshow("Translated", translated)

# ROTATION
# def rotate(img, angle, rotationPoint=None):
#   (height, width) = img.shape[:2]
#   if rotationPoint is None:
#     rotationPoint = (width//2, height//2)
#   rotationMatrix = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
#   dimensions = (width, height)
#   return cv.warpAffine(img, rotationMatrix, dimensions)

# rotated = rotate(img, -45)
# cv.imshow("Rotated", rotated)

# RESIZING (INTER_AREA FOR SMALLER, INTER_LINEAR OR CUBIC FOR LARGER)
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# cv.imshow("Resized", resized)

# FLIP (0 = Y, 1 = X, -1 = XY)
# flip = cv.flip(img, 0)
# cv.imshow("Flipped", flip)

# CROPPING (USING ARRAY SLICING)
cropped = img[200:400, 200:300]
cv.imshow("Cropped", cropped)

# cv.imshow("Lady", img)
cv.waitKey(0)