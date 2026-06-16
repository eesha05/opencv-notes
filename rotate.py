import cv2
"""
M = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, M, (width, height))
angle in degrees
scale how much to zoom in or out
1.0 is same 0.5 is half and 2.0 is double
centre is passed generally width//1 and height//2
width and height is the new size of the image
"""
image=cv2.imread("parrot image.jpg")
(w,h)=image.shape[:2]
M=cv2.getRotationMatrix2D((w//2,h//2),105,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("rotated image",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
to flip an image or to image an image across a line
flipped=cv2.flip(image,flipole)
flip pole tells the opencv in which way to flip the image
0 for vertically ie top to bottom
1 for horizontally ie left to right
-1 for both
"""
flipped=cv2.flip(image,-1)
cv2.imshow("flipped image",flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()