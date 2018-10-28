import cv2
import numpy as  np
import pyautogui

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade= cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

cap=cv2.VideoCapture(0)
count=0
while True:
	ret,img=cap.read()
	img=cv2.flip(img,1)
	img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	face=face_cascade.detectMultiScale(img_gray,1.2,4)

	for (x,y,w,h) in face:
		cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
		roi_gray=img_gray[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]
		eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
		
		if eyes==():
			count+=1
			font = cv2.FONT_HERSHEY_SIMPLEX
			T="blinked"
			cv2.putText(img, str(T) ,(20,60), font, 4,(0,0,255),2,cv2.LINE_AA)
			pyautogui.press('up')

		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 
	cv2.imshow('img',img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()        	
