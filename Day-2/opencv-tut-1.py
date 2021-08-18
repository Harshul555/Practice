import cv2
import imutils

image = cv2.imread(r'C:\Users\Harshul Gupta\Desktop\Practice\Day-2\jp.jpg')
(h, d, w) = image.shape
print("width = {}, height = {}, depth = {}".format(w, h, d))
#(B, G, R) = image[100,50]
#print("R={}, G={}, B={},".format(R, B, G))
#roi = image[60:160, 320:420]
#cv2.imshow("ROI", roi)
#cv2.imshow("Image", image)

#resized = cv2.resize(image, (200,200))
#cv2.imshow("Fixed Resizing", resized)

#r = 50.0/w
#dim = (int(h*r), 50)
#resized = cv2.resize(image, dim)
#cv2.imshow("Aspect Ratio Resize", resized)

#resized = imutils.resize(image, width=300)
#cv2.imshow("Imutils Resize", resized)

#center = (w//2, h//2)
#M = cv2.getRotationMatrix2D(center, -45, 1.0)
#rotated = cv2.warpAffine(image, M, (w,h))
#cv2.imshow("OpenCV rotation", rotated)

#rotated = imutils.rotate(image, -45)
#cv2.imshow('Imutils Rotation', rotated)

#rotated = imutils.rotate_bound(image, 45)
#cv2.imshow("Imutils Bound Rotation", rotated)

#blurred = cv2.GaussianBlur(image, (11,11), 0)
#cv2.imshow("Blurred", blurred)

#output = image.copy()
#cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
#cv2.imshow("Rectangle", output)

#cv2.circle(output, (320, 150), 20, (255, 0, 0), -1)
#cv2.imshow("Circle", output)

#cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
#cv2.imshow("Line", output)

output = image.copy()
cv2.putText(output, "OpenCv + Jurassic Park!!", (10, 25),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)