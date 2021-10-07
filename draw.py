import cv2 as cv
import numpy as np

# CREATE A BLANK ARRAY OF ZEROS WITH DTYPE uint8 AS A CANVAS FOR DRAWING
# ARGS ARE HEIGHT, WIDTH AND THE NUMBER OF COLOR CHANNELS (BGR, so 3)
blank = np.zeros((500, 500, 3), dtype="uint8")

# IMAGE MANIPULATION PRACTICE
# 1. PAINT THE IMAGE A CERTAIN COLOR
# blank[200:300, 300:400] = 0,255,0 # CAN USE [:] TO TARGET ALL PIXELS
# cv.imshow("Green", blank)

# 2. DRAW A RECTANGLE
# ARGS ARE THE IMG TO DRAW OVER, TWO POINTS, A COLOR, A THICKNESS AND A LINETYPE
# cv.rectangle(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (0,255,0), thickness=-1)

# 3. DRAW A CIRCLE
# cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (0,0,255), thickness=1)

# 4. DRAW A LINE
# cv.line(blank, (100, 250), (300, 400), (0,255,0), thickness=2)

# 5. WRITE TEXT
cv.putText(blank, "Hello!", (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow("Line", blank)

# img = cv.imread("photos/cat.jpg")
# cv.imshow("Cat", img)

cv.waitKey(0)