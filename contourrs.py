"""contours is the outline of the image which gives the shape of the binary 
(black and white)image, make image from canny or thresholding
mode is retrival mode it tells how many and what kind of contours to return
retrieval external only returns the outer most shape
retrieval tree returns all the shapes
retrieval list returns all except heiarchy
method is approximation method how much detail to retail for each countour
this function returns list of all outlines detected in a shift
heirarchy is the relationship of all the outlines returned to contours variable
"""
#contours, hierarchy = cv2.findContours(image, mode, method)
import cv2

img = cv2.imread("traingle shape.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)#_ means one more value will come but i will not need this
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2. imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows ()
#function to draw the contours on the top of the original image
#cv2.drawContours(image, contours, contour_index, color, thickness)
#contour index is which shape to draw if 0 draw 1st shape, 1 draw second and -1 draw all


