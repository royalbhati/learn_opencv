import cv2

image=cv2.imread("img.jpeg")

(b,g,r)=image[500,500]


print("Red {}  Green {}  Blue {} before changing values".format(r,g,b))

image[0:500,0:500]=(0,0,255)


(b,g,r)=image[500,500]

print("Red {}  Green {}  Blue {} after changing values".format(r,g,b))



cv2.imshow("image",image)

cv2.waitKey(0) 