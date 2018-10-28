import cv2
import numpy as np

video_cap=cv2.VideoCapture(0)

while True:# We repeat infinitely (until break):
	_,frame=video_cap.read() # We get the last frame.
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# image = cv2.GaussianBlur(image, (7, 7), 0)
	# image=cv2.cv2.bilateralFilter(image,9,41,41)
	# image = cv2.Canny(image, 80,100)
	(_,thresh)=cv2.threshold(image,185,255,cv2.THRESH_BINARY_INV)
	image=cv2.flip(thresh,1)
	image=cv2.convexHull(image, returnPoints=False)
	print(len(image))
	# lap = cv2.Laplacian(image, cv2.CV_64F)
	# lap = np.uint8(np.absolute(lap))

	cv2.imshow("Canny", image)
	if cv2.waitKey(1) & 0xFF == ord('q'): # If we type on the keyboard:
		break    
            
        
video_cap.release() # We turn the webcam off.
cv2.destroyAllWindows()



























(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# How many contours did we find?
print("I count {} coins in this image".format(len(cnts)))

# Let's highlight the coins in the original image by drawing a
# green circle around them
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

# Now, let's loop over each contour
for (i, c) in enumerate(cnts):
	# We can compute the 'bounding box' for each contour, which is
	# the rectangle that encloses the contour
	(x, y, w, h) = cv2.boundingRect(c)

	# Now that we have the contour, let's extract it using array
	# slices
	print("Coin #{}".format(i + 1))
	coin = image[y:y + h, x:x + w]
	cv2.imshow("Coin", coin)

	# Just for fun, let's construct a mask for the coin by finding
	# The minumum enclosing circle of the contour
	mask = np.zeros(image.shape[:2], dtype = "uint8")
	((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
	cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
	mask = mask[y:y + h, x:x + w]
	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
	cv2.waitKey(0)




