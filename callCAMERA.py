# coding=utf-8

import cv2
camera_id = 0
cap = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)#cv2.CAP_DSHOW是作为open调用的一部分传递标志，还有许多其它的参数，而这个CAP_DSHOW是微软特有的。
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc("M","J","P","G"))
while True:
  ret, frame = cap.read()
  cv2.imshow("window1",frame)
 
  if cv2.waitKey(1)&0xFF == ord("q"):
   break

cap.release()
cv2.destroyAllWindows()
