import cv2
import numpy as np

canvas=np.zeros((300,300,3),dtype='uint8')

orange=(0,80,200)

cv2.line(canvas , (0,100),(300,0),orange , 1)
cv2.line(canvas , (0,110),(300,0),orange , 1)
cv2.line(canvas , (0,120),(300,0),orange , 1)
cv2.line(canvas , (0,130),(300,0),orange , 1)
cv2.line(canvas , (0,140),(300,0),orange , 1)


cv2.line(canvas , (0,0),(300,100),orange , 1)
cv2.line(canvas , (0,0),(300,110),orange , 1)
cv2.line(canvas , (0,0),(300,120),orange , 1)
cv2.line(canvas , (0,0),(300,130),orange , 1)
cv2.line(canvas , (0,0),(300,140),orange , 1)

gray=(200,200,220)

cv2.line(canvas , (150,0),(150,100),gray, 1)


cv2.circle(canvas,(150,100),20,(255,255,255))
cv2.circle(canvas,(150,100),15,gray)
cv2.circle(canvas,(150,100),10,gray)


blue=(255,0,0)
cv2.line(canvas , (150,110),(10,200),blue , 1)
cv2.line(canvas , (150,110),(40,200),orange , 1)
cv2.line(canvas , (150,110),(80,200),blue , 1)
cv2.line(canvas , (150,110),(120,200),orange , 1)
cv2.line(canvas , (150,110),(200,200),blue , 1)
cv2.line(canvas , (150,110),(250,200),orange , 1)
cv2.line(canvas , (150,110),(280,200),blue , 1)


cv2.rectangle(canvas,(0,200),(300,300),gray,5)


cv2.imshow("im",canvas)

cv2.waitKey(0)
