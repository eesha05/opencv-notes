import cv2
"""
to draw a line 
cv2.line(img, pt1, pt2, color, thickness)
(0,0) is the top left corner of the image
x is top to bottom and y is left to right 
(x,y) is one point
"""
image=cv2.imread("parrot image.jpg")
color=(250,0,0)
cv2.line(image,(2,20),(100,500),color,4)
cv2.imshow("line in an image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
to draw a rectangle
cv2.rectangle(img, pt1, pt2, color, thickness)
pt1 is top left corner of rect
pt2 is bottom right corner of rect
"""
cv2.rectangle(image, (2,20), (100,550), color, 4)
cv2.imshow("rectangle in an image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
to draw a circle 
cv2.circle(img, center, radius, color, thickness)
radius is in pixels
if thickness is -1 thein it fills the circle with a color
"""
cv2.circle(image, (150,150), 150, color, 10)
cv2.imshow("circle in an image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()