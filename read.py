# IMPORT COMPUTER VISION PACKAGE
import cv2 as cv

# IMAGES -----------------------------------------------------------

# TAKE THE PATH OF AN IMAGE AS AN ARG AND RETURN A MATRIX OF PIXELS
# img = cv.imread("photos/cat.jpg")

# TAKES A PIXEL MATRIX AND DISPLAYS IN A NEW WINDOW
# args: Name of the window, pixel matrix;
# cv.imshow("Cat", img)

# USE TO HOLD WINDOWS OPEN UNTIL KEY PRESS
# cv.waitKey(0)

# VIDEOS -----------------------------------------------------------
# READ A VIDEO FILE
# args: integer for local cameras, path for video file
capture = cv.VideoCapture("videos/dog.mp4")

# WHILE READING A VIDEO WITH OCV, YOU READ FRAME BY FRAME WITH A WHILE LOOP
while True:
  # RETURNS True TO IsTrue IF FRAME SUCCESSFULLY READ
  # frame REPRESENTS THE CURRENT FRAME OF THE VIDEO
  isTrue, frame = capture.read()

  if isTrue:
    # EACH ITERATION, SHOW THE CURRENT FRAME OF THE VIDEO IN THE VIDEO WINDOW
    cv.imshow("Video", frame)

    # HONESTLY I HAVE NO IDEA BUT IT SAID TO PUT THIS TO BREAK THE TRUE LOOP
    # EXPLAINS THAT IF THE LETTER D IS PRESSED IT BREAKS THE LOOP
    if cv.waitKey(20) & 0xFF == ord("d"):
      break
  else:
    break

# RELEASE THE CAPTURE DEVICE SO THAT IT CAN BE USED ELSEWHERE AND DESTROY UNNEEDED WINDOWS
capture.release()
cv.destroyAllWindows()

# -215 ASSERTION FAILED ERROR LIKELY MEANS PATH DOESN'T HAVE A MEDIA FILE
# ALSO HAPPENS WHEN A VIDEO RUNS OUT OF FRAMES