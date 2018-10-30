import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_blue = np.array([100,100,100])
upper_blue = np.array([120,255,255])

points = []

ret,frame = cap.read()
Height,Width = frame.shape[:2]
print(Height,Width)
frame_count = 0

while True :
    ret,frame = cap.read()
    hsv_img = cv2. cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_img,lower_blue, upper_blue)

    _,contours,_ = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    center = int(Height/2),int(Width/2)

    if len(contours)>0:
        c = max(contours,key = cv2.contourArea)
        (x,y),radius = cv2. minEnclosingCircle(c)
        M = cv2.moments(c)
        try:
            center = (int(M['m10']/M['m00']),int(M['m01']/M['m00']))
        except:
            center = int(Height/2),int(Width/2)
        if radius > 25:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,0,255),2)
            cv2.circle(frame,center,5,(0,255,0),-1)
    points.append(center)

    if radius > 25:
        for i in range(1,len(points)):
            try:
                cv2.line(frame,points[i-1],points[i],(0,255,0),2)
            except:
                pass
        frame_count = 0
    else:
        frame_count+=1
        if frame_count == 10:
            points = []
            frame_count = 0
    frame = cv2.flip(frame,1)
    cv2.imshow("object",frame)
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()