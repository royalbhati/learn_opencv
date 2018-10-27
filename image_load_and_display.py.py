import cv2

image=cv2.imread("img.jpeg")

print("image height",image.shape[0])
print("image width",image.shape[1])
print("image channels",image.shape[2])

cv2.imshow("image",image)

cv2.waitKey(0) 