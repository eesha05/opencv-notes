import cv2
image=cv2.imread("parrot image.jpg")
"""
cropped_image = image[startY: endY, startX: endX]
to cut part of the image because images are just 2d or 3d array
y axis is rows ie pixels from top to bottom
x axis is columns that is pixels from left to right
end not included
"""
cropped=image[150:200,130:220]
cv2.imshow("cropped image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
