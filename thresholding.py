import cv2


img=cv2.imread("img.jpeg")


(_,thresh)=cv2.threshold(img,185,255,cv2.THRESH_BINARY_INV)

cv2.imshow("im",thresh)
cv2.waitKey(0)