"""detects the outline of the image,detects borders and separate objects,feature extraction
finds edges where brightness suddenly changes
threshold 1 is lower boundary to detect weak edges
threshold 2 is upper boundary to detect strong edges
threshold is cutoff for brightness if lesser than threshold then make it 0
and if slightly greater than upper then convert to 255 bascically make every pixel either 0 or 1
this is also called thresholding
image must be a grayscale image"""
#edges = cv2.Canny(image, threshold1, threshold2)
import cv2
image=cv2.imread("parrot image.jpg",cv2.IMREAD_GRAYSCALE)
edges= cv2.Canny(image, 50, 150)
cv2.imshow("canny image",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

#thresholded_image = cv2. threshold(image, thresh_value, max_value, method)
ret,thresh_img= cv2.threshold(image,120,255,cv2.THRESH_BINARY)
cv2.imshow("thresh hold image",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
