import cv_helper as cvh
import cv2

img=cv2.imread("img.jpeg")


# cv2.imshow("im",cvh.translate(img,500,120))s

# cv2.waitKey(0)

# cv2.imshow("im",cvh.rotate(img,(500,120),60,0.5))
# cv2.imshow("im",cvh.img_blur(img,'gaussian',(7,7)))

# cv2.waitKey(0)

cv2.imshow("im",cvh.img_blur(img,'bilateral',(7,7)))


cv2.waitKey(0)