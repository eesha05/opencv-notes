import cv2
image=cv2.imread("parrot image.jpg")
"""
to add text in an image
cv2.putText(img, text, org, font, fontScale, color, thickness)
org is the bottom left corner of the text ie a point
font is font type
fontScale is size of the font 1.0 is normal and 2.0 is big
"""
cv2.putText(image, "hello", (10,400), cv2.FONT_ITALIC,1.5, (255,0,0),4)
cv2.imshow("text written in an image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()