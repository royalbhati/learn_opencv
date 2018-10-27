import cv2
import numpy as np


def translate(img,x,y):
	M=np.float32([[1,0,x],[0,1,y]]) # matrix o show how much to shift the image (+ve x means right and -ve left )
									# +ve y is down and -ve y up
	shifted=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

	return shifted


def rotate(img,pointOfRotation,angle,scale):
	M=cv2.getRotationMatrix2D(pointOfRotation,angle,scale)
	rotated=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
	return rotated


def resize(img,w,h=None):
	'''
	w = width of image you want as output

	h= default is None 
	'''

	if h==None:
		print(img.shape)
		dim=(w,int((w/img.shape[1])*img.shape[0]))
		print(dim)
		resized=cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
		return resized
	else:
		resized=cv2.resize(img,(w,h),interpolation = cv2.INTER_AREA)	
		return resized

def flip(img,factor):
	'''
	1 -flip the image horizontally, around the y-axis.
	0 - indicates that we want to flip the image vertically, around the x-axis 
   -1 - flips the image around both axes.
	'''
	flipped=cv2.flip(img,factor)
	return flipped


def split_channel(img,return_channel):
	'''
	return_channel : B, G , R
	B- Blue channel
	G- Green channel
	R- Red channel
	'''
	# zeros = np.zeros(img.shape[:2], dtype = "uint8")
	(B,G,R)=cv2.split(img)

	if return_channel=='B':
		return B
	elif return_channel=='G':
		return G
	else:
		return R	

def img_blur(img,blur_type,kernel_size):
	if blur_type==None:
		blurred=cv2.blur(img,kernel_size)
		return blurred
	# elif blur_type==('Gaussian') or ('gaussian'):
	# 	blurred=cv2.GaussianBlur(img,kernel_size)
	# 	return blurred
	elif blur_type=='bilateral':
		blurred=cv2.bilateralFilter(img,9,41,41)
		return blurred	
	else:
		blurred=cv2.medianBlur(img,kernel_size[0])
		return blurred

			
