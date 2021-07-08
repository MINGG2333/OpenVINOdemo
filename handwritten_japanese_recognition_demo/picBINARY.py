import cv2 as cv
picpath = 'data/try1.jpg'
filepath = 'data/try11.png'
img = cv.imread(picpath)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thresholdValue, two_value = cv.threshold(gray, 0, 255, cv.THRESH_BINARY |cv.THRESH_OTSU)
cv.imwrite(filepath,two_value)
cv.imshow('thresholdGlob', two_value)
cv.waitKey(0)

