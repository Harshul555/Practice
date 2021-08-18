import numpy as np
import argparse
import cv2

def edge_mask(img, line_size, blur_value):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray_blur = cv2.medianBlur(gray, blur_value)
	edges = cv2.adaptiveThreshold(gray_blur, 255,
	 cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
	return edges

def color_quantization(img, k):
	#Transform the image
	data = np.float32(img).reshape((-1,3))

	#Determine criteria
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

	#Implementing K-mean
	ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	center = np.uint8(center)
	result = center[label.flatten()]
	result = result.reshape(img.shape)
	return result



line_size = 7
blur_value = 7	
total_color = 9
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = 'path to input image')
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
image = img.copy()

edges = edge_mask(img, line_size, blur_value)
img = color_quantization(img, total_color)

blurred = cv2.bilateralFilter(img, d=7, sigmaColor = 230, sigmaSpace = 200)

cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)

cv2.imshow("Quantized", img)
cv2.imshow("Original",image)
cv2.imshow("Cartoon",cartoon)
cv2.waitKey(0)