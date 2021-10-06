import cv2 as cv

# A FUNCTION THAT TAKES A FRAME AND SCALE MULTIPLIER, SCALES X & Y AXIS AND RETURNS THE RESIZED FRAME
def rescaleFrame(frame, scale=0.75):
  # MULTIPLE HEIGHT BY THE SCALE MULTIPLIER
  height = int(frame.shape[0] * scale)
  # MULTIPLE WIDTH BY THE SCALE MULTIPLIER
  width = int(frame.shape[1] * scale)
  # ESTABLISH NEW FRAME DIMENSIONS
  dimensions = (width, height)

  # RETURN THE SCALED FRAME
  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# SCALE AN IMAGE --------------------------------------------------------------------------------------
# img = cv.imread("photos/cat_large.jpg")
# cv.imshow("Cat", rescaleFrame(img, 0.25))

# cv.waitKey(0)

# SCALE AN VIDEO --------------------------------------------------------------------------------------
video = cv.VideoCapture("videos/dog.mp4")

while True:
  isTrue, frame = video.read()

  if isTrue:
    cv.imshow("Video", rescaleFrame(frame))

    if cv.waitKey(20) & 0xFF == ord("d"):
      break
  else:
    break

video.release()
cv.destroyAllWindows()